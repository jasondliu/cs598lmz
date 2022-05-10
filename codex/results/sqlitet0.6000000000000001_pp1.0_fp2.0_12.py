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

def my_cb_destroy(p):
    del my_threading_local.a

def fn_cb(p):
    print(p)
    return p

def fn_cb_destroy(p):
    pass

def fn_cb_step(p, n_col, cols, vals):
    print(p, n_col, cols, vals)
    return 0

def fn_cb_final(p):
    print(p)
    return 0

def fn_cb_destroy(p):
    pass

def my_init():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
    lib.sqlite3_open.restype = ctypes.c_int
    lib.sqlite3_create_function.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.
