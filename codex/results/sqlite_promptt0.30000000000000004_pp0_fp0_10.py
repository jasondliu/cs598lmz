import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

from . import _sqlite3

class SQLite3_Exception(Exception):
    def __init__(self, errstr):
        self.errstr = errstr

    def __str__(self):
        return self.errstr

class SQLite3_Connection(object):
    def __init__(self, dbname):
        self.dbname = dbname
        self.db = None
        self.lock = threading.Lock()
        self.connect()

    def connect(self):
        self.db = sqlite3.connect(self.dbname)

    def close(self):
        if self.db is not None:
            self.db.close()
            self.db = None

    def execute(self, sql, params=()):
        with self.lock:
            if self.db is None:
                self.connect()
            try:
                self.db.execute(sql, params)
            except sqlite3.Error as e:
                raise SQLite3_Exception(e.args[0])

    def execut
