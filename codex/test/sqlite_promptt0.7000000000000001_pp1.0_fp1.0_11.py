import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# http://stackoverflow.com/questions/3190869/pass-sqlite-connection-from-one-thread-to-another-thread

# Define new data types
class c_sqlite3(ctypes.Structure):
    pass
c_sqlite3._fields_ = [
    ('_opaque_struct', ctypes.c_int)
]

class c_sqlite3_stmt(ctypes.Structure):
    pass
c_sqlite3_stmt._fields_ = [
    ('_opaque_struct_1', ctypes.c_int),
    ('_opaque_struct_2', ctypes.c_int)
]


# Load the SQLite shared library
sqlite3_lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

# Declare the SQLite functions we want to use
sqlite3_open = sqlite3_lib.sqlite3_open
sqlite3_open.restype = ctypes.c_int
sqlite3_
