import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('pythonsqlite.db')

class MyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class _SQLite3:
    def __init__(self, **kwargs):
        self.sqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
        self.sqlite3.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
        self.sqlite3.sqlite3_open.restype = ctypes.c_int
        self.sqlite3.sqlite3_close.argtypes = [ctypes.c_void_p]
        self.sqlite3.sqlite3_close.restype = ctypes.c_int
        self.sqlite3.sqlite3_prepare_v2.argtypes = [ctypes.c_void_p, ctypes.c_char_
