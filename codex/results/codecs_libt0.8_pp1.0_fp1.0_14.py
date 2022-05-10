import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from creds import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
from models import Base

engine = create_engine('mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'
                       .format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME),
                       pool_recycle=3600)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.create_all(engine)
