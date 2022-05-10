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
    if hasattr(my_threading_local, 'a'):
        del my_threading_local.a
    return 1

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

lib.sqlite3_set_authorizer(None, my_cb, ctypes.c_void_p())
lib.sqlite3_set_authorizer(None, my_cb2, ctypes.c_void_p())

conn = sqlite3.connect(DB_URI, uri=True)

assert conn.execute("select test(1, 2)").fetchone()[0] == 1
