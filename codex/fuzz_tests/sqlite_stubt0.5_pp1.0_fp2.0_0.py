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
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))

    lib.sqlite3_enable_shared_cache(ctypes.c_int(1))

    conn = ctypes.c_void_p()

    conn_p = ctypes.pointer(conn)

    lib.sqlite3_open(ctypes.c_char_p(DB_URI.encode('utf-8')), conn_p)

    lib.sqlite3_prepare_v2(conn, "SELECT test(?, ?)", -1, ctypes.c_void_p(), ctypes.c_void_p())
