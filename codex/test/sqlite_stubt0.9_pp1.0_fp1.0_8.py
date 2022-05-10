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

def get_db():
    if not hasattr(my_threading_local, "a"):
        with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as a:
            a.create_function("test", 1, my_fn)
            my_threading_local.a = a
    return my_threading_local.a

libsqlite3.sqlite3_proxy_initialize.restype = ctypes.c_int
libsqlite3.sqlite3_proxy_initialize.argtypes = [ctypes.c_void_p, ctypes.c_int]
libsqlite3.sqlite3_proxy_initialize.argtypes = [
    ctypes.CFUNCTYPE(
        ctypes.c_int,
        ctypes.c_void_p,
    ),
    ctypes.c_int
]


libsqlite3.sqlite3_proxy_test.restype = ctypes.c_uint8
