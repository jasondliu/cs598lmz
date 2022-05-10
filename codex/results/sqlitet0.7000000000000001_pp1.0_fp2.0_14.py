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

class TestSQLite3:
    def test_create_function(self):
        lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.p))
        lib.sqlite3_create_function(my_threading_local.p.value, b"test", 2, my_threading_local.p.value, my_cb, None, None)
        lib.sqlite3_close(my_threading_local.p.value)

    def test_create_collation(self):
        lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.p))
        lib.sqlite3_create_collation(my_threading_local.p.value, b"test", 1, my_threading_local.
