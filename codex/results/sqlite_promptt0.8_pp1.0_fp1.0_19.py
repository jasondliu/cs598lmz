import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class SQLDB:
  def __init__(self):
    self.db = None
    self.lock = threading.Lock()

  def connect(self):
    self.db = sqlite3.connect(":memory:")
    return self.db

  def execute(self, stmt, args):
    self.lock.acquire()
    self.db.execute(stmt, args)
    self.lock.release()

  def executemany(self, stmt, args):
    self.lock.acquire()
    self.db.executemany(stmt, args)
    self.lock.release()

  def select(self, stmt, args = None):
    self.lock.acquire()
    if not args:
      self.db.select(stmt)
    else:
      self.db.select(stmt, args)
    self.lock.release()

  def cursor(self):
    return self.db.cursor()

  def commit(self):
    self.lock.acquire()

