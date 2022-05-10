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

def test_sqlite_threading():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.close()

    del my_threading_local.a

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.close()

def test_sqlite_threading_destructor():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.close()

    del my_threading_local.a

    conn = sqlite3.connect(DB_URI, uri=True)
    del conn
    gc.collect()

def test_sqlite_threading_destructor_2():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my
