import ctypes
import ctypes.util
import threading
import sqlite3

from boxpi.config import config
from boxpi.util.datetime import get_datetime, get_formatted

__version__ = "0.0.1"


class DB():

    def __init__(self):
        libname = ctypes.util.find_library("sqlite3")
        if libname is None:
            raise Exception("could not find libary")
        self.libsqlite3 = ctypes.CDLL(libname)
        self.libsqlite3.sqlite3_config(1, 1)

    def open_db(self, path):
        path_bytes = bytes(path, "utf-8")
        self.db = ctypes.py_object(
            self.libsqlite3.sqlite3_open(path_bytes, ctypes.c_void_p(0)))

    def close_db(self):
        if self.db:
            self.libsqlite3.sqlite3_close(self.db)
