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

def test_init():
    sqlite3.sqlite3_initialize()
    assert sqlite3.sqlite3_libversion_number() > 3007000
    assert sqlite3.sqlite_version_info >= (3, 7, 8)
    assert sqlite3.sqlite_version == sqlite3.sqlite_version_info
    assert sqlite3.sqlite_version_number == sqlite3.sqlite3_libversion_number()

def test_open():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    assert isinstance(a, sqlite3.Connection)
    assert isinstance(a, deleting_conn)
    a.close()
    del a

def test_open_kwargs():
    a = sqlite3.connect(database=":memory:", uri=True, factory=deleting_conn)
    assert isinstance(a, sqlite3.Connection)
    assert isinstance(a, deleting_conn)
    a.close()
    del a
