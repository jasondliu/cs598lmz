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
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.close()
    del a
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b.close()
    del b
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.close()
    del c
    d = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    d.close()
    del d
    e = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    e.close()
    del e
    f = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    f.close()
   
