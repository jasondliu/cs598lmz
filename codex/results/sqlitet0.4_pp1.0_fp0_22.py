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
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_shutdown()
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_initialize()
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_config(ctypes.c_int(4), my_cb, None)

    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b.execute("select test(1, 2)")
    b.execute("select test(1, 2)")
    del b

    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.execute("select test(1, 2)")
    c.execute("select test(1, 2)")
    del c

    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_shutdown()
   
