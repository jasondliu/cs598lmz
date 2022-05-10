import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')


class SQLite3Connector:
    def __init__(self, db_name):
        self.db_name = db_name
        self.sqlite3_libname = ctypes.util.find_library('sqlite3')
        self.sqlite3_lib = ctypes.CDLL(self.sqlite3_libname)
        self.sqlite3_lib.sqlite3_threadsafe()
        # 1.create threading lock (mutex)
        self.mutex = threading.Lock()
        # 2.create threading condition
        self.cond = threading.Condition(self.mutex)
        self.PROTOCOL = 1
        self.SHAREDCACHE = 2
        self.OPEN_READWRITE = 0x00000002
        self.OPEN_CREATE = 0x00000004
        self.OPEN_URI = 0x00000040
        self.OPEN_NOMUTEX = 0x00008000
        self.OPEN_FULLMUTEX = 0x00010000
        self.OP
