import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
class Database(object):
    def __init__(self, *args, **kwargs):
        self.conn = sqlite3.connect(":memory:")
        self.conn.row_factory = sqlite3.Row
        if "database" in kwargs:
            with open(kwargs["database"], "r") as f:
                self.conn.executescript(f.read())
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.execute("PRAGMA busy_timeout = 10000")
        self.cursor = self.conn.cursor()
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
        
    def __enter__(self):
        self.cursor = self.conn.cursor()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor = None

class Library(object):
    
    def _load_
