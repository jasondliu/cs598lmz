import ctypes
import ctypes.util
import threading
import sqlite3
import os.path

# internal SQLite defines and types
SQLITE_STATIC = ctypes.c_void_p(0)
SQLITE_TRANSIENT = ctypes.c_void_p(-1)
class sqlite3_stmt(ctypes.Structure):
    pass

# sqlite3_exec() flags
SQLITE_OK = 0
SQLITE_ERROR = 1
SQLITE_INTERNAL = 2
SQLITE_PERM = 3
SQLITE_ABORT = 4
SQLITE_BUSY = 5
SQLITE_LOCKED = 6
SQLITE_NOMEM = 7
SQLITE_READONLY = 8
SQLITE_INTERRUPT = 9
SQLITE_IOERR = 10
SQLITE_CORRUPT = 11
SQLITE_NOTFOUND = 12
SQLITE_FULL = 13
SQLITE_CANTOPEN = 14
SQLITE_PROTOCOL = 15
SQLITE_EMPTY = 16
SQLITE_SCHEMA = 17
SQLITE_TOOBIG = 18
