import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Original(Base):
    __tablename__ = 'original'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(Text(250), nullable=False)
 
class Translated(Base):
    __tablename__ = 'translated'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(Text(250), nullable=False)
    original_id = Column(Integer, ForeignKey('original.id'))
    original = relationship(Original)
 
# Create
