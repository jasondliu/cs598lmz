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
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_open(":memory:", ctypes.byref(ctypes.c_void_p()))

lib.sqlite3_create_function(ctypes.c_void_p(), "test", 2, 1, ctypes.c_void_p(), my_cb, None, None)

lib.sqlite3_create_function(ctypes.c_void_p(), "test2", 2, 1, ctypes.c_void_p(), my_cb2, None, None)

def my_thread():
    lib.sqlite3_exec(ctypes.c_void_p(),
