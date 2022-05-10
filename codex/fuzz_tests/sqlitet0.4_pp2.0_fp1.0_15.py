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

def my_cb2(p):
    my_threading_local.a.close()
    return 1

def my_cb3(p):
    my_threading_local.a.close()
    return 1

def my_cb4(p):
    my_threading_local.a.close()
    return 1

def my_cb5(p):
    my_threading_local.a.close()
    return 1

if __name__ == "__main__":
    sqlite3.enable_callback_tracebacks(True)

    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_initialize()

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("my_cb", 0, my_cb)
    conn.create_function("my_cb2", 0, my_cb2)
    conn.create_function("my_cb3", 0, my_cb
