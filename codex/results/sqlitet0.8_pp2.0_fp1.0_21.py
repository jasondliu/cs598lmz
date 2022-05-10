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

if __name__ == "__main__":
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.create_function("my_cb", 1, my_cb)

    l = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    a = l.sqlite3_open_v2("test", ctypes.byref(ctypes.c_voidp()), 1, None)
    p = l.sqlite3_malloc(100)
    l.sqlite3_result_text(p, "foo", 3, 0)

    try:
        l.sqlite3_create_function(a, b"my_cb", 1, 1, p, None, None, None)
        l.sqlite3_prepare_v2(a, b"SELECT my_cb('hello')", 100, ctypes.byref(ctypes.c_voidp()), None)
        l.sqlite3_step(p)
    finally:
        l.sqlite3_finalize(p)
