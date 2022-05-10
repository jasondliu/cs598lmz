import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm.collections import attribute_mapped_collection

from datetime import datetime
from _mysql_exceptions import MySQLError
from pytz import timezone


from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime,
    Text,
    Float,
    Boolean,
    ForeignKey)
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr


Base = declarative_base()


class ProtNoVersion(Base):
    __tablename__ = '
