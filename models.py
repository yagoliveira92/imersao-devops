from sqlalchemy import Column, Identity, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    curso_id = Column(Integer, ForeignKey("cursos.id"))

    aluno = relationship("Aluno", back_populates="matriculas")
    curso = relationship("Curso", back_populates="matriculas")

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    telefone = Column(String(255), nullable=False)

    matriculas = relationship("Matricula", back_populates="aluno")

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    nome = Column(String(255), nullable=False)
    codigo = Column(String(255), nullable=False, unique=True) 
    descricao = Column(Text)  

    matriculas = relationship("Matricula", back_populates="curso")