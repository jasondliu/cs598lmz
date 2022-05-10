import ctypes
import ctypes.util
import threading
import sqlite3
import os


def get_lib():
    lib = ctypes.util.find_library('sqlite3')
    if lib is None:
        raise Exception('Library sqlite3 not found')
    return lib


class SQLite3(object):
    def __init__(self, lib=None):
        if lib is None:
            lib = get_lib()
        self.lib = ctypes.CDLL(lib)
        self.lib.sqlite3_threadsafe()
        self.lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
        self.lib.sqlite3_open.restype = ctypes.c_int
        self.lib.sqlite3_close.argtypes = [ctypes.c_void_p]
        self.lib.sqlite3_close.restype = ctypes.c_int
        self.lib.sqlite3_prepare_v2.argtypes = [ctypes.c_void_p, ctypes.c_
