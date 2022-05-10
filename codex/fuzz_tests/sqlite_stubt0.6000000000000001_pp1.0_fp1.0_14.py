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
    my_threading_local.a.execute('select test(1, 2)')
    return 1

def my_cb3(p):
    my_threading_local.a.close()
    return 1

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    cb_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    cb_ptr2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb2)
    cb_ptr3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb3)

    lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, None]
    lib
