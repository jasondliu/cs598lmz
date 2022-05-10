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

def my_cb_delete(p):
    if hasattr(my_threading_local, "a"):
        del my_threading_local.a
    return 1

def my_create_fn(p, a, b, c, d):
    return 1

def my_step_fn(p, a, b, c, d):
    return 1

def my_final_fn(p):
    return 1

def my_destroy_fn(p):
    return 1

sql_functions = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
sqlite3_create_function = sql_functions.sqlite3_create_function
sqlite3_create_function.argtypes = (
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    c
