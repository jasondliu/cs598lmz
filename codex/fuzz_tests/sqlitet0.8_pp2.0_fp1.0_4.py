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

libc = ctypes.CDLL(ctypes.util.find_library("c"))

cb = sqlite3.SQLiteErrorHandler(my_cb)

libc.calloc.restype = ctypes.c_void_p

test_conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn, errorhandler=cb)

test_conn.close()

del test_conn
del cb

conns = []

for i in range(10):
    test_conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.a = test_conn
    test_conn.close()
    conns.append(my_threading_local.a)
    del my_threading_local.a
    del test_conn

for conn in conns:
    conn.close()
