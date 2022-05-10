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

def my_cb_2(p):
    my_threading_local.a.close()
    return 1

def my_cb_3(p):
    return my_threading_local.a.test(2, 3)

def my_cb_4(p):
    return my_threading_local.a.test(2, 3)

def my_cb_5(p):
    return my_threading_local.a.test(2, 3)

my_cb_2_t = sqlite3.SQLITE_DETERMINISTIC | sqlite3.SQLITE_UTF8 | sqlite3.SQLITE_INNOCUOUS

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_create_function_v2.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_void_p,
   
