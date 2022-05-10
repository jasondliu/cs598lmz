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
    a = my_threading_local.a
    assert a.execute("select test(1, 2)").fetchone()[0] == 1
    return 1

callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
callback2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb2)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
lib.sqlite3_open.restype = ctypes.c_int
lib.sqlite3_create_function.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c
