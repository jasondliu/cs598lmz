import ctypes
import ctypes.util
import threading
import sqlite3
import os

class LibSqlite:
    def __init__(self, db_path):
        self.libsqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.libsqlite.sqlite3_open.restype = ctypes.c_int
        self.libsqlite.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
        self.libsqlite.sqlite3_close.argtypes = [ctypes.c_void_p]
        self.libsqlite.sqlite3_prepare_v2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_void_p)]
        self.libsqlite.sqlite3_step.argtypes = [ctypes.c_void_p]
