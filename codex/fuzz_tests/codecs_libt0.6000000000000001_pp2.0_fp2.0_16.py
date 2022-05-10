import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.schema import UniqueConstraint

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50), unique=True)
    orders = relationship('Order', backref='customer')

    def __repr__(self):
        return "<Customer('%s')>" % (self.name)

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=
