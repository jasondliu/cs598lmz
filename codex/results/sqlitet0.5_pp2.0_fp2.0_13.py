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

def my_cb2(a):
    my_threading_local.a.close()
    my_threading_local.a = None

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
    lib.sqlite3_open.restype = ctypes.c_int
    lib.sqlite3_enable_load_extension.argtypes = [ctypes.c_void_p, ctypes.c_int]
    lib.sqlite3_enable_load_extension.restype = ctypes.c_int
    lib.sqlite3_load_extension.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
    lib.sqlite3_load_extension.restype = c
