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

def cb_deleter(p):
    del my_threading_local.a

def main():
    lib_path = ctypes.util.find_library("sqlite3")
    if lib_path is None:
        raise Exception("sqlite3 not found")
    lib = ctypes.CDLL(lib_path)
    ptr = lib.sqlite3_threadsafe()
    if ptr == 0:
        raise Exception("this sqlite3 is not threadsafe")
    lib.sqlite3_config(3, 1)
    my_cb_p = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    cb_deleter_p = ctypes.CFUNCTYPE(None)(cb_deleter)
    del_cb_p = ctypes.POINTER(ctypes.CFUNCTYPE(None))(cb_deleter_p)
    lib.sqlite3_thread_cleanup(del_cb_p)
