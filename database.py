from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import oracledb
# Configuração da conexão com o Oracle Autonomous Database
# As credenciais são lidas a partir de variáveis de ambiente
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
connect_string = os.environ.get("CONNECT_STRING")

# String de conexão para o Oracle
DATABASE_URL = f"oracle+oracledb://{db_user}:{db_password}@{connect_string}"


engine = create_engine(
	f'oracle+oracledb://:@',
	connect_args={
        'user': db_user,
        'password': db_password,
        'dsn': connect_string,
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()