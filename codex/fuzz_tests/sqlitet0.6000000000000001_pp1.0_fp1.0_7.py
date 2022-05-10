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

def test_fn(a, b):
    return a

def my_cb_2(p):
    a = my_threading_local.a
    assert a

    a.create_function("test", 2, test_fn)

    return 1

def my_cb_3(p):
    a = my_threading_local.a
    assert a

    a.create_function("test", 2, test_fn)

    return 1

# test_cb_1 has a memory leak of a deleting_conn class
def test_cb_1():
    a = sqlite3.connect(":memory:")
    a.create_function("test", 2, test_fn)
    a.commit()

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_progress_handler.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p), ctypes.c
