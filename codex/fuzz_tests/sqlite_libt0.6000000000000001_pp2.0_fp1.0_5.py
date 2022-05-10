import ctypes
import ctypes.util
import threading
import sqlite3
import time

class DynamicLibrary:
    def __init__(self, name):
        self.name = name
        self.lib = ctypes.CDLL(ctypes.util.find_library(name))

    def __getattr__(self, name):
        return getattr(self.lib, name)

class TimeoutException(Exception):
    pass

# TODO: replace this with a proper C extension
class SQLite3(DynamicLibrary):
    def __init__(self, filename):
        DynamicLibrary.__init__(self, 'sqlite3')
        self.filename = filename
        self.db = ctypes.c_void_p()
        self.open()

    def open(self):
        self.check(self.sqlite3_open(self.filename.encode('utf-8'), ctypes.byref(self.db)))

    def close(self):
        self.check(self.sqlite3_close(self.db))

    def check(self, result):
        if result != 0:
            raise RuntimeError(self.sql
