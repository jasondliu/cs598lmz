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

libsqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite.sqlite3_config_uri(1)
libsqlite.sqlite3_uri_boolean(DB_URI, "readonly", 1)
libsqlite.sqlite3_uri_boolean(DB_URI, "immutable", 1)
libsqlite.sqlite3_config(ctypes.c_int(libsqlite.SQLITE_CONFIG_URI), ctypes.c_int(my_cb), None)

del libsqlite
del deleting_conn

def test():
    a = sqlite3.connect(DB_URI, uri=True)
    yield 1

def test_fn(a, b):
    return a

for i in range(100):
    test()
    a = my_threading_local.a
    a.create_function("test", 2, test_fn)
    for j in range(100):
        a.execute("SELECT test(?, ?)", (1, 2)).fetchone
