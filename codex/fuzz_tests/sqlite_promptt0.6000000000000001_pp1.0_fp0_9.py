import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memorydb?mode=memory&cache=shared', uri=True).
#if sys.platform == 'darwin':
#    # On Mac OS X, dlopen() does not take relative paths.
#    _sqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
#else:
#    _sqlite = ctypes.CDLL('libsqlite3.so')
_sqlite = ctypes.CDLL('libsqlite3.so')

SQLITE_OK = 0
SQLITE_ROW = 100
SQLITE_DONE = 101
SQLITE_INTEGER = 1
SQLITE_FLOAT = 2
SQLITE_TEXT = 3
SQLITE_BLOB = 4
SQLITE_NULL = 5

class sqlite_int64(ctypes.c_longlong):
    def __repr__(self):
        return str(self.value)

class sqlite_uint64(ctypes.c_ulonglong):
    def __repr__(self):
        return str(self.value)
