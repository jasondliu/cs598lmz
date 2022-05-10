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

def my_int_convert(n):
    return int(n)

if __name__ == '__main__':
    cdll = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    my_cb_p = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    ret = cdll.sqlite3_open_v2(b":memory:", ctypes.byref(ctypes.c_void_p()), 2, None)
    ret = cdll.sqlite3_create_function_v2(ctypes.c_void_p(), b"my_int", 1, 1, None, my_int_convert, None, None, None)
    ret = cdll.sqlite3_progress_handler(ctypes.c_void_p(), 1, my_cb_p, None)

    conn = sqlite3.connect(DB_URI, uri=True)
    print(conn.execute("select test(5, 6)").fetchone())
    print(conn
