import ctypes
import ctypes.util
import threading
import sqlite3
import signal
import types
import time
import math
from ctypes import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.dialects.postgresql import BIT
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.pool import NullPool
from sqlalchemy import exc
from sqlalchemy.event import listen
from datetime import datetime
#from mediainfo import getinfo

#import data

#from hdf5 import acquire

#from hdf5engine import acquire
from data5 import acquire

#####DataBase
Base = declarative_base()

class Image(Base):
	__tablename__ = 'image'
	id = Column(Integer, primary_key=True)
	#signal_id
