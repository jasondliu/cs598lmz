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

def my_new(_self):
    _self = _self.__new__(_self)
    _self.register_bu()
    return _self

my_sqlite3 = sqlite3.sqlite_version_info

class MyConn(sqlite3.Connection):
    pass

def my_factory(a, b, c, d, e):
    return MyConn(a, b, c, d, e)


class MyDB(sqlite3.Connection):
    def __init__(self, uri):
        sqlite3.Connection.__init__(self, uri, factory=my_factory)

class MyConn(sqlite3.Connection):
    pass

def my_factory_new(a, b, c, d, e):
    return MyConn(a, b, c, d, e)

class MyDB(sqlite3.Connection):
    def __init__(self, uri):
        sqlite3.Connection.__init__(a, b, factory=my_factory_new)

class
