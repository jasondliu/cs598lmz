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

def test_functions():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    lib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()), 2, None)
    lib.sqlite3_create_function_v2(ctypes.c_void_p(), b"test", 2, 1, cb, None, None, None)
    lib.sqlite3_close_v2(ctypes.c_void_p())
    assert my_threading_local.a.execute("select test(1, 2)").fetchone()[0] == 1

if __name__ == "__main__":
    test_functions()
