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

class my_db_factory(object):
    def __init__(self, uri):
        self.uri = uri

    def __call__(self, *args, **kwargs):
        return sqlite3.connect(self.uri, *args, **kwargs)

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(1, my_cb, None)
    conn = sqlite3.connect(DB_URI, uri=True, factory=my_db_factory(DB_URI))
    conn.execute("create table test (a integer)")
    conn.execute("insert into test values (test(1, 2))")
    conn.execute("select * from test")
    conn.close()
    conn = sqlite3.connect(DB_URI, uri=True, factory=my_db_factory(DB_URI))
    conn.execute("select * from test")
    conn.close()

