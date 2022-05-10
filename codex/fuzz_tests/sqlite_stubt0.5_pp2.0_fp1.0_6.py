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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_initialize()
lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
lib.sqlite3_open_v2.restype = ctypes.c_int
lib.sqlite3_open_v2(DB_URI.encode(), ctypes.c_void_p(), 0, ctypes.c_char_p(0))
lib.sqlite3_create_function_v2(ctypes.c_void_p(), b"test", 2, 1, ctypes.c_void_p(), my_cb, None, None, None)

def test_fn(a, b):
    return a

conn = sqlite3.connect(DB_URI, uri=True)
conn.create_function("test", 2, test_fn)

cur = conn
