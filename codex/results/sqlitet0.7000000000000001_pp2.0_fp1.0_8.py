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

def test_uri_test_factory():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    c_my_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    p = lib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()), 6, None)

    p = lib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()), 6, None)

    lib.sqlite3_create_function_v2(p, b"test", 2, 1, 0, c_my_cb, None, None, None)

    lib.sqlite3_close(p)
</code>
I get the following traceback:
<code>Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.
