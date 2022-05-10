import _struct

from collections import namedtuple
from datetime import datetime

from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa.types import LongType, DateType

from constants import *

class Base(object):
  """
  Base class for all Cassandra objects
  """
  def __init__(self, column_family, row_key, column_family_dict,
               column_key_type=DateType(),
               column_value_type=LongType()):
    self.column_family = column_family
    self.row_key = row_key
    self.column_family_dict = column_family_dict
    self.column_key_type = column_key_type
    self.column_value_type = column_value_type

  @property
  def _pool(self):
    return ConnectionPool(CASSANDRA_KEYSPACE, CASSANDRA_HOSTS)

