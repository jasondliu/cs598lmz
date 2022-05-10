import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/var/lib/sqlite3/pysqlite.db')

class Sqlite3Ext(sqlite3.Connection):
    def __init__(self, *args, **kwargs):
        self.lock = threading.Lock()
        sqlite3.Connection.__init__(self, *args, **kwargs)

    def cursor(self, *args, **kwargs):
        return CursorExt(self.lock, self, *args, **kwargs)

class CursorExt(sqlite3.Cursor):
    def __init__(self, lock, *args, **kwargs):
        self.lock = lock
        sqlite3.Cursor.__init__(self, *args, **kwargs)

    def execute(self, *args, **kwargs):
        with self.lock:
            return sqlite3.Cursor.execute(self, *args, **kwargs)

class Database(object):
    def __init__(self, path):
        self.lock = threading.Lock()
        self.path = path
       
