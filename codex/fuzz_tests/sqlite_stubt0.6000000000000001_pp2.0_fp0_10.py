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

def my_cb_destroy(p):
    my_threading_local.a.close()

    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)

    # load sqlite3
    sqlite3_path = ctypes.util.find_library("sqlite3")
    sqlite3_lib = ctypes.CDLL(sqlite3_path)
    sqlite3_lib.sqlite3_config(5, 1) # enable threading

    # load sqlite3_ext
    sqlite3_ext_path = ctypes.util.find_library("sqlite3_ext")
    sqlite3_ext_lib = ctypes.CDLL(sqlite3_ext_path)

    # load sqlite3_ext_init
    sqlite3_ext_init = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(("sqlite3_ext_init", sqlite3_ext_lib))
    sqlite3_ext_init(None)

    # load
