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

p = ctypes.POINTER(sqlite3.sqlite3)()

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_open_v2(DB_URI.encode("ascii"), ctypes.byref(p), 1, None)

libsqlite3.sqlite3_enable_load_extension(p, 1)
libsqlite3.sqlite3_load_extension(p, "./build/enable_load_extension.so".encode("ascii"), b"my_cb", None)

with sqlite3.connect(DB_URI, uri=True) as conn:
    assert my_threading_local.a is not None
    assert conn is my_threading_local.a
