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

def make_sqlite_fn():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_set_authorizer.argtypes = [ctypes.c_void_p, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)]

    # This is the crux of the whole test: the function in the second argument
    # is a Python function that has access to a Python object (the Connection).
    #
    # If the Connection is not correctly refcounted, this will cause a crash
    # because the Connection will be destroyed before the SQLite callback
    # returns.
    lib.sqlite3_set_authorizer(
        sqlite3.sqlite_version_info,
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
        )

def test_sqlite_fn():
    make_sqlite_fn()

    conn = sqlite3.connect(DB_URI, ur
