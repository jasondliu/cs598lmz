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
    driver = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    driver.sqlite3_open.restype = ctypes.c_void_p
    driver.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
    open_callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(my_cb)
    driver.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.c_void_p,
                                       ctypes.c_int, ctypes.c_char_p]
    driver.sqlite3_open_v2.restype = ctypes.c_void_p
    driver.sqlite3_open_v2(DB_URI, ctypes.c_void_p(), 1, None)
    driver.sqlite3_open_v2(DB_URI, ctypes.c_void_p(), 1, open_callback
