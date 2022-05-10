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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_config(ctypes.c_int(0x0004), my_cb, None)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.execute("create table test (a)")

del a

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.execute("insert into test values (test(1, 2))")

del a

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.execute("select test(1, 2) from test")

del a

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.execute("select test(1, 2) from test")

del a

a = sqlite3.connect(DB_URI, uri=
