import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared')

try:
    import sqlite3
except ImportError:
    from pysqlite2 import dbapi2 as sqlite3

import os
import time
import unittest

import test_cases

def _load_sqlite():
    libsqlite3 = ctypes.util.find_library('sqlite3')
    if not libsqlite3:
        raise RuntimeError('sqlite3 library not found')
    return ctypes.CDLL(libsqlite3)

# sqlite3_open_v2 flags
SQLITE_OPEN_READONLY = 0x00000001
SQLITE_OPEN_READWRITE = 0x00000002
SQLITE_OPEN_CREATE = 0x00000004
SQLITE_OPEN_URI = 0x00000040
SQLITE_OPEN_MEMORY = 0x00000080
SQLITE_OPEN_NOMUTEX = 0x00008000
SQLITE_OPEN_FULLMUTEX =
