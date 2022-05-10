import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(), sqlite3.version, sqlite3.sqlite_version,
# sqlite3.threadsafety
print("sqlite3.connect: ", sqlite3.connect(""))
print("sqlite3.version: ", sqlite3.version)
print("sqlite3.sqlite_version: ", sqlite3.sqlite_version)
print("sqlite3.threadsafety: ", sqlite3.threadsafety)

# Check the declaration of sqlite3_stmt for later use

import sys
print("THREAD SAFETY: ", sys.platform, sys.version, ctypes.sizeof(ctypes.c_size_t), ctypes.sizeof(ctypes.c_void_p))
_libsqlite = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
try:
    _libsqlite.sqlite3_column_name.argtypes = [ctypes.c_void_p, ctypes.c_int]
except AttributeError:
    print("SKIP")
    sys.exit()

# Check the
