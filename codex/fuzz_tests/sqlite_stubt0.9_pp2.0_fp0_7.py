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

cb = ctypes.cast(my_cb, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p))

path = ctypes.util.find_library("sqlite3")
dll = ctypes.CDLL(path)
dll.sqlite3_initialize()
dll.sqlite3_config(ctypes.c_int(5), cb, 0)
dll.sqlite3_finalize(ctypes.c_int(5))

my_threading_local.a = sqlite3.connect(DB_URI)
my_threading_local.a.close()

from test import dbapi20
suite = dbapi20.DatabaseAPI20Test(DB_URI, None, row_factory=None)

suite.test_fetchall()
