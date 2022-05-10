import gc, weakref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy_utils import ChoiceType

Base = declarative_base()

class MyClass(Base):
    __tablename__ = 'my_class'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    cls = Column(ChoiceType(('A', 'B', 'C')))

class MySubClass(MyClass):
    __tablename__ = 'my_sub_class'
    id = Column(Integer, ForeignKey(MyClass.id), primary_key=True)
    number = Column(Integer)
    __mapper_args__ = {'polymorphic_identity': 'my_sub_class'}

class MyDeepSubClass(MySubClass):
    __tablename__ = 'my_deep_sub_class'
    id = Column(Integer, ForeignKey(
