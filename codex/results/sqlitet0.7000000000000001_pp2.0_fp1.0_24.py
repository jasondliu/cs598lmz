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

def my_cb_fail(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 0

if __name__ == "__main__":
    libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    libsqlite3.sqlite3_shutdown.restype = None
    libsqlite3.sqlite3_shutdown.argtypes = []
    libsqlite3.sqlite3_initialize.restype = None
    libsqlite3.sqlite3_initialize.argtypes = []

    libsqlite3.sqlite3_config.restype = None
    libsqlite3.sqlite3_config.argtypes = [
        ctypes.c_int,
    ]

    libsqlite3.sqlite3_
