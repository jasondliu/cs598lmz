import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import and_, or_
from sqlalchemy import text
import json
from datetime import datetime
import time
import sys

#sys.path.append('/home/ubuntu/workspace/python/utils')
sys.path.append('../utils')
import utils
import config_vars

# Set up database
engine = create_engine(config_vars.database_connection_string, echo=False)
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)

def add_users
