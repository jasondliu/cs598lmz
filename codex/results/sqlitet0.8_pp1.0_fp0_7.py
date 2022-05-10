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
    result = sqlite3.sqlite3_open("test", ctypes.byref(ctypes.c_void_p()))
    if result != 0:
        raise Exception("Failed to open SQLite DB")

    result = sqlite3.sqlite3_open_v2("test", ctypes.byref(ctypes.c_void_p()),
                                     sqlite3.SQLITE_OPEN_READWRITE |
                                     sqlite3.SQLITE_OPEN_CREATE |
                                     sqlite3.SQLITE_OPEN_FULLMUTEX |
                                     sqlite3.SQLITE_OPEN_MEMORY,
                                     None)
    if result != 0:
        raise Exception("Failed to open SQLite DB")

    my_threading_local.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.a.row_factory = sqlite3.Row

    print("Before we register the callbacks:")
   
