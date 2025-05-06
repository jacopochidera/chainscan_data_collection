# Scripts/models.py

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

from Scripts.database import Base  # use the shared Base!


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(128), nullable=False)  # Store hashed password

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
