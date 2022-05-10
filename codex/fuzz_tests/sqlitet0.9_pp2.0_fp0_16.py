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
    t = my_threading_local.a
    t.clear_bindings()
    t.isolation_level = "DEFERRED"
    t.row_factory = sqlite3.Row
    t.set_authorizer(lambda x, y, z, t: 0)
    with t as c:
        c.execute('select 1')


libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_create_function.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p
    ]
libsqlite3.sqlite3_create_function.restype = ctypes.c_int
libsqlite3.sql
