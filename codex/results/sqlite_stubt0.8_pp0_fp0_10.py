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

my_cb_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

lib = ctypes.util.find_library("sqlite3")
lib = ctypes.CDLL(lib)

def main():
    buf = ctypes.create_string_buffer(256)

    lib.sqlite3_config(ctypes.c_int(4), my_cb_cb, ctypes.py_object(my_threading_local))

    lib.sqlite3_open(DB_URI, ctypes.byref(ctypes.c_void_p()))
    lib.sqlite3_close(ctypes.c_void_p())

main()
