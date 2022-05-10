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


if __name__ == '__main__':
    mylib = ctypes.CDLL(ctypes.util.find_library('sqlite3'), use_errno=True)
    mylib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
    mylib.sqlite3_open_v2.restype = ctypes.c_int

    mylib.sqlite3_config.argtypes = [ctypes.c_int, ctypes.c_void_p]
    mylib.sqlite3_config.restype = ctypes.c_int

    mylib.sqlite3_config(ctypes.c_int(7), ctypes.c_void_p(my_cb))

    conn = dbapi2.connect(DB_URI, uri=True)
    c1 = conn.cursor()
    c2 = conn.cursor()

