import ctypes
import ctypes.util
import threading
import sqlite3

#pylint: disable=invalid-name,line-too-long

class SQLite3Exception(Exception):
  """ Class to throw SQLite3 Exceptions in Python  """


def sqlite3_threadsafe():
  """ Is SQLite Threadsafe """

  return sqlite3.threadsafety != 0


libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))


def sqlite3_open(filename):
  """ Open an SQLite Database """

  _out = ctypes.POINTER(sqlite3)()
  _result = libsqlite3.sqlite3_open(filename.encode("utf-8"), ctypes.byref(_out))
  if _result == 0:
    return _out.contents
  raise SQLite3Exception(sqlite3_errmsg())


def sqlite3_close(conn):
  """ Close an SQLite Database """

  conn = ctypes.cast(ctypes.pointer(conn), ctypes.POINTER(ctypes.c_void_p))
  _result
