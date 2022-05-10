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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
cb = lib.sqlite3_set_authorizer(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb), 0)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

conn.create_function("test", 2, test_fn)

cur = conn.cursor()
cur.execute("select test(1,2)")

cur = my_threading_local.a.cursor()
cur.execute("select test(1,2)")
