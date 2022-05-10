import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

try:
    import _sqlite3
except ImportError:
    pass

# TODO:
# - test with threading=0
# - test with UTF-8
# - test with different encodings
# - test with a real database
# - test with other time functions

# Some constants from sqlite3.h
SQLITE_OK = 0
SQLITE_ROW = 100
SQLITE_DONE = 101
SQLITE_INTEGER = 1
SQLITE_FLOAT = 2
SQLITE_TEXT = 3
SQLITE_BLOB = 4
SQLITE_NULL = 5

SQLITE_UTF8 = 1

SQLITE_TRANSIENT = -1

# Some constants from sqlite3ext.h
SQLITE_OPEN_READONLY = 1
SQLITE_OPEN_READWRITE = 2
SQLITE_OPEN_CREATE = 4


# TODO: Get rid of this?
def load_sqlite_functions(libsqlite3, functions):
    for func in functions:
        setattr(libsqlite3,
