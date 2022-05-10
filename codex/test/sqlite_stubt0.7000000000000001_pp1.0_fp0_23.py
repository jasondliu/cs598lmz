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

def my_cb_free(p):
    del my_threading_local.a
    return 1

def main():
    sqlite_lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    sqlite_lib.sqlite3_progress_handler.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p), ctypes.c_void_p]

    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    cb_free = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb_free)

    p = sqlite_lib.sqlite3_progress_handler(sqlite3.sqlite_version_info, 1, cb, cb_free)

    print("test")
    my_threading_local.a
