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
    my_threading_local.a.close()

    return 1

def my_cb3(p):
    return 1

def my_cb4(p):
    my_threading_local.a.close()

    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()))

lib.sqlite3_collation_needed16.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
lib.sqlite3_create_collation16.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
lib.sqlite3_create_collation16.restype = ctypes.c_int
