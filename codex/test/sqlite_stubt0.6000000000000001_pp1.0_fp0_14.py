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

def main():
    lib = ctypes.util.find_library("sqlite3")
    if not lib:
        raise Exception("sqlite3 not found")
    lib = ctypes.CDLL(lib)

    my_cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    my_cb_ptr = my_cb_type(my_cb)

    lib.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.conn))
    lib.sqlite3_exec(my_threading_local.conn, "SELECT test(1, 2)", None, None, None)
    lib.sqlite3_close(my_threading_local.conn)

    lib.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.conn))
    lib.sqlite3_exec(my_threading_local.conn, "SELECT test(1, 2)", None, None, None)
