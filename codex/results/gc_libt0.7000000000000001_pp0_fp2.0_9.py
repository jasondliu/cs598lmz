import gc, weakref
import types
import inspect
import sys

#
import common.v101.config as conf
#from base import *
from pysqlite2 import dbapi2 as sqlite
import logging
from common.v101.exceptions import RowNotFound,NoSuchTable
from common.v101.loaders import DBF,CSV,XLS,XLSX,XML
from common.v101.base import Base as Parent

from common.v101.base import *

from pylog import *
#import config.config as conf
e=sys.exit

class Base(Parent):
	"""Base class for all DBs"""
	def __init__(self,log=None,print_sql=0,sql='',db=None,**kwargs):
		global gc
		#self.db=db
		#self.log=log
		self.print_sql=print_sql
		self.sql=sql
		self.kwargs=kwargs
		self.db=db
		self.log=log
		self.log
