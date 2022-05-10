import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def my_cb2(p):
    return 1

def my_cb3(p):
    return 1

# This test is only useful on 32-bit platforms.
if sizeof(c_void_p) == 4:
    # Initialize callbacks
    c_cb = CFUNCTYPE(c_int, c_void_p)(my_cb)
    c_cb2 = CFUNCTYPE(c_int, c_void_p)(my_cb2)
    c_cb3 = CFUNCTYPE(c_int, c_void_p)(my_cb3)

    # Initialize libsqlite
    libsqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    # Register callbacks
    libsqlite.sqlite3_test_control(6, c_cb2)
    libsqlite.sqlite3_test_control(7, c_cb3)
    libsqlite.sqlite3_test_control(8, c_cb)

    # Create a connection
