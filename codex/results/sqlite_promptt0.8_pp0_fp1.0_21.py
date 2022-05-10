import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# Find and load the library.
libname = ctypes.util.find_library('sqlite3')
if libname is None:
    raise Exception('Cannot find the sqlite3 library')
sqlite3 = ctypes.CDLL(libname)

sqlite3.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
sqlite3.sqlite3_open.restype = ctypes.c_int

sqlite3.sqlite3_close.argtypes = [ctypes.c_void_p]
sqlite3.sqlite3_close.restype = ctypes.c_int

conn = ctypes.c_void_p()
status = sqlite3.sqlite3_open(':memory:', ctypes.byref(conn))
if status != 0:
    raise Exception('Cannot create connection to sqlite3 database')

sqlite3.sqlite3_close(conn)

# Run sqlite3.connect(':
