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

def another_cb():
    print(my_threading_local.a)
    return 0

def third_cb():
    return "fourth callback"

if __name__ == "__main__":
    assert ctypes.util.find_library("sqlite3") is not None
    print(ctypes.util.find_library("sqlite3"))

    clib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    assert clib.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(my_threading_local.lib), 2, None) == 0

    my_threading_local.lib = lib = sqlite3.Connection(DB_URI)
    assert my_threading_local.lib is lib

    cb_v3_fn = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    another_cb_v3_fn = ctypes.CFUNCTYPE(ctypes.c_int,
