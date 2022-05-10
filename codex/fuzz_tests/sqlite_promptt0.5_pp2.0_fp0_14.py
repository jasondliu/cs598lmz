import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared")

# Python 2/3 compatibility
try:
    unicode
except NameError:
    unicode = str

# PyPy compatibility
try:
    import __pypy__
    PYPY = True
except ImportError:
    PYPY = False

# Python 2/3 compatibility
try:
    unicode
except NameError:
    unicode = str

# PyPy compatibility
try:
    import __pypy__
    PYPY = True
except ImportError:
    PYPY = False

# For some reason, ctypes.util.find_library("sqlite3") returns None
# in PyPy 2.0.  But this works...
sqlite_lib = ctypes.util.find_library("sqlite3") or "sqlite3"
_sqlite = ctypes.CDLL(sqlite_lib)

# Some constants from the SQLite3 C header file
SQLITE_OK = 0
SQLITE_ROW = 100
SQLITE_DONE = 101

SQLITE_TRANSI
