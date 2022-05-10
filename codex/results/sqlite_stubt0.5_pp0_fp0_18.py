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
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def main():
    sqlite3.enable_shared_cache(True)
    dll = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    dll.sqlite3_enable_shared_cache(True)
    dll.sqlite3_config(1)
    dll.sqlite3_config(3, ctypes.cast(my_cb, ctypes.c_void_p))
    dll.sqlite3_config(4, ctypes.cast(my_cb2, ctypes.c_void_p))

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(
