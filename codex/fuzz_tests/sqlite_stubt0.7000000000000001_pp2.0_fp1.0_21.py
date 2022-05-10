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

def test_conn():
    a = sqlite3.connect(DB_URI)
    del a

def test_close():
    a = sqlite3.connect(DB_URI)
    a.close()
    del a

def test_close_after_finalize():
    a = sqlite3.connect(DB_URI)
    a.create_function("test", 2, lambda a, b: a)
    del a

def test_close_after_finalize_after_gc():
    a = sqlite3.connect(DB_URI)
    a.create_function("test", 2, lambda a, b: a)
    del a
    gc.collect()

def test_thread():
    e = python_sqlite.sqlite3_enable_shared_cache(1)
    sqlite3.enable_shared_cache(1)

    a = sqlite3.connect(DB_URI)
    a.create_function("test", 2, lambda a, b: a)

    my_threading_local.a = a

    t
