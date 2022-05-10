import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Find and load the sqlite3 shared library
sqlite3_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

# Set the return types of some functions
sqlite3_lib.sqlite3_open.restype = ctypes.c_int
sqlite3_lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
sqlite3_lib.sqlite3_close.argtypes = [ctypes.c_void_p]
sqlite3_lib.sqlite3_busy_timeout.argtypes = [ctypes.c_void_p, ctypes.c_int]
# Test sqlite3.connect()
# - DONE: connect
# - DONE: busy_timeout
# - DONE: close
# - TODO: connect_with_file_uri

def test_connect():
    db = sqlite3.connect(":memory:")
    assert db._handle is not None
    db.close()
