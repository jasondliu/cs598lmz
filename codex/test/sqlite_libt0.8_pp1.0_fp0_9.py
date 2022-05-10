import ctypes
import ctypes.util
import threading
import sqlite3
from queue import *
from helper import *

class sqlite_api:
    def __init__(self):
        self.sqlite = ctypes.cdll.LoadLibrary('./libsqlite.so')
        self.sqlite.alloc_sqlite()
        self.sqlite.sqlite_open.restype = ctypes.c_void_p
        self.sqlite.sqlite_exec.restype = ctypes.c_void_p
        self.sqlite.sqlite_execute_done.restype = ctypes.c_bool
        self.sqlite.sqlite_prepare_insert.restype = ctypes.c_void_p
        self.sqlite.sqlite_get_insert_data.restype = ctypes.c_void_p
        self.sqlite.sqlite_prepare_read.restype = ctypes.c_void_p
        self.sqlite.sqlite_get_read_data.restype = ctypes.c_void_p
        self.sqlite.sqlite_prepare_delete.restype
