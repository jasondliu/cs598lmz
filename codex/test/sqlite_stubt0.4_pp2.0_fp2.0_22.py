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
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_open_v2(DB_URI.encode('utf-8'), ctypes.byref(my_threading_local.a), 0x00000004 | 0x00000001, None)
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_create_function_v2(my_threading_local.a, b"test", 2, 1, None, my_cb, None, None, None)
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_close(my_threading_local.a)

