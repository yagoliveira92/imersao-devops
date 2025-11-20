from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

import oracledb
import os

# Configuração da conexão com o Oracle Autonomous Database
# As credenciais são lidas a partir de variáveis de ambiente
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_dsn = os.environ.get("DB_DSN")

# String de conexão para o Oracle
DATABASE_URL = f"oracle+oracledb://{db_user}:{db_password}@{db_dsn}"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


