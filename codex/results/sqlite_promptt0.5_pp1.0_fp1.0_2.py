import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

class TinyDB(object):
    def __init__(self, db_path):
        lib_path = ctypes.util.find_library("sqlite3")
        self.lib = ctypes.CDLL(lib_path)
        self.lib.sqlite3_open.restype = ctypes.c_int
        self.lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
        self.lib.sqlite3_close.restype = ctypes.c_int
        self.lib.sqlite3_close.argtypes = [ctypes.c_void_p]
        self.lib.sqlite3_exec.restype = ctypes.c_int
        self.lib.sqlite3_exec.argtypes = [
            ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p,
            ctypes.c_void_p]
        self.lib.sqlite3_errmsg
