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

def check_threading_local():
    assert my_threading_local.a
    assert my_threading_local.a.execute("SELECT test(1, 2)").fetchone()[0] == 1

class my_obj(object):
    def __init__(self):
        self.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(self, a, b):
        return a

    def __del__(self):
        self.a.close()

class my_obj2(object):
    def __init__(self):
        self.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def __del__(self):
        self.a.close()

def test_obj():
    x = my_obj()
    x.a.create_function("test", 2, x.test_fn)
    assert x.a.execute("SELECT test(1, 2)").fetchone()[
