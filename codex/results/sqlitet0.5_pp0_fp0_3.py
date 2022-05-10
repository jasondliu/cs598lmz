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
    my_threading_local.a = None

    return 1

def main():
    lib = ctypes.util.find_library("sqlite3")
    if not lib:
        print("Could not find libsqlite3")
        return 1

    sqlite3 = ctypes.CDLL(lib)

    sqlite3.sqlite3_initialize()

    my_cb_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    my_cb2_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb2)

    sqlite3.sqlite3_thread_cleanup.argtypes = []
    sqlite3.sqlite3_thread_cleanup.restype = None

    sqlite3.sqlite3_thread_set_callback(my_cb_ptr, my_cb2_ptr)

   
