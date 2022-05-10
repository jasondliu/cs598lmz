import ctypes
import ctypes.util
import threading
import sqlite3
import traceback
import datetime
import logging
import os, stat
import os.path

logger = logging.getLogger(__name__)

class DataStorage(threading.Thread):
  """
  A class to write data to a database
  """
  def __init__(self, dbFile, name, columns, dataBuffer, dataBufferLock):
    """
    Initialization
    
    @param dbFile        : database file
    @param name          : table name
    @param columns       : column names and types
    @param dataBuffer    : data buffer
    @param dataBufferLock: data buffer lock
    """
    threading.Thread.__init__(self)
    self._dbFile = dbFile
    self._name = name
    self._columns = columns
    self._dataBuffer = dataBuffer
    self._dataBufferLock = dataBufferLock
    self._createTable()

  def _createTable(self):
    """
    Create table if it doesn't exist
    """
