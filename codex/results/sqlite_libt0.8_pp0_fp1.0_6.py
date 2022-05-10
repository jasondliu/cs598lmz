import ctypes
import ctypes.util
import threading
import sqlite3
import os
import mmap

_root_path = os.path.dirname(os.path.abspath(__file__))

_c_tm = ctypes.cdll.LoadLibrary(ctypes.util.find_library("m"))
_c_tm.tm_malloc.argtypes = [ctypes.c_size_t]
_c_tm.tm_free.argtypes = [ctypes.c_void_p]
_c_tm.tm_free.restype = ctypes.c_void_p

def tm_malloc(size):
    return _c_tm.tm_malloc(size)


class TMGet(object):
    def __init__(self, sql, max_rows=0, param=None, orderby=None):
        self.max_rows = max_rows
        self.cols = None
        self.rows = 0
        self.sql = sql
        self.param = param
        self.orderby = orderby
        conn = sqlite3.connect(":memory:")
        cursor =
