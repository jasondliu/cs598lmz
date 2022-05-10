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

def my_cb_dealloc(p):
    my_threading_local.a = None

    return 1

def my_cb_fn(p):
    if p == 1:
        return my_cb_dealloc(p)
    return my_cb(p)

def main():
    lib = ctypes.util.find_library("sqlite3")
    sqlite3 = ctypes.CDLL(lib)

    sqlite3.sqlite3_enable_shared_cache(1)
    sqlite3.sqlite3_config(1, my_cb_fn)

    t1 = threading.Thread(target=lambda: sqlite3.sqlite3_open(DB_URI.encode(), ctypes.byref(ctypes.c_void_p())))
    t2 = threading.Thread(target=lambda: sqlite3.sqlite3_open(DB_URI.encode(), ctypes.byref(ctypes.c_void_p())))

    t1.start()
    t2.start()

    t1.join
