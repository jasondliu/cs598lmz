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

def main():
    lib = ctypes.util.find_library("sqlite3")
    if not lib:
        raise Exception("Cannot find sqlite3 library")
    sqlite3 = ctypes.CDLL(lib)
    sqlite3.sqlite3_open.restype = ctypes.c_int
    sqlite3.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
    sqlite3.sqlite3_exec.restype = ctypes.c_int
    sqlite3.sqlite3_exec.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p)]
    sqlite3.sqlite3_close.restype = ctypes.c_int
    sql
