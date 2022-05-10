import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# This is a hack to make sure that the sqlite3 module is loaded before
# we try to load the sqlite3 library.
sqlite3.connect(':memory:')

# Load the sqlite3 library.
lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

# Set the SQLITE_OPEN_NOMUTEX flag.
lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
lib.sqlite3_open_v2.restype = ctypes.c_int

# Open a connection to a database.
db = ctypes.c_void_p()
lib.sqlite3_open_v2(':memory:', ctypes.byref(db), 0x00040000, None)

# Create a table.
