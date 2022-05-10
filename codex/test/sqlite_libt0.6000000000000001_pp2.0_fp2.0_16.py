import ctypes
import ctypes.util
import threading
import sqlite3
from collections import namedtuple
import os
from contextlib import contextmanager
from . import utils
from . import settings
from . import log

class Error(Exception):
    pass

class NotSupportedError(Error):
    pass

def _get_sqlite3_functions():
    path = ctypes.util.find_library('sqlite3')
    if not path:
        raise RuntimeError("Can't find sqlite3 library")
    lib = ctypes.CDLL(path)
    if not lib:
        raise RuntimeError("Can't load sqlite3 library")
    lib.sqlite3_open.restype = ctypes.c_int
    lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
    lib.sqlite3_close.restype = ctypes.c_int
    lib.sqlite3_close.argtypes = [ctypes.c_void_p]
    lib.sqlite3_exec.restype = ctypes.c_int
