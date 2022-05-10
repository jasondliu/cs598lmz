import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
import weakref

from . import sqlite3_connection
from . import sqlite3_cursor

import logging
logger = logging.getLogger(__name__)

# SQLite constants
SQLITE_OK = 0
SQLITE_ROW = 100
SQLITE_DONE = 101
SQLITE_INTEGER = 1
SQLITE_FLOAT = 2
SQLITE_BLOB = 4
SQLITE_NULL = 5
SQLITE3_TEXT = 3

# SQLite execution flags
SQLITE_STATIC = ctypes.c_void_p(0)
SQLITE_TRANSIENT = ctypes.c_void_p(-1)

# SQLite API
sqlite3_open = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open
sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
sqlite3_open.restype = ctypes.c_
