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
lib.sqlite3_set_authorizer.argtypes = (ctypes.c_void_p, ctypes.CFUNCTYPE(c_int, c_void_p))
lib.sqlite3_set_authorizer.restype = None

lib.sqlite3_open_v2.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), c_int, ctypes.c_char_p)
lib.sqlite3_open_v2.restype = c_int

p = c_void_p(0)
lib.sqlite3_open_v2(c_char_p(DB_URI.encode("utf-8")), ctypes.byref(p), c_int(1), None)
lib.sqlite3_set_authorizer(p, my_cb)
