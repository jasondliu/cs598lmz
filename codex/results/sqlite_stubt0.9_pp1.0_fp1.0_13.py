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
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    a.set_authorizer(my_cb)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    def bar(*a):
        return a

    a.set_busy_handler(bar)

    # initialize the sqlite library
    global sqlite_lib
    sqlite_lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

    ctx = sqlite3.create_collation('mycoll', a.text_factory, sqlite_lib.mycompare)

    assert(a.create_collation('mycoll', a.text_factory, sqlite_lib.mycompare) is ctx)

    cur = a.cursor()

    def mycheck(a, b):
        return a

    cur.set_authorizer(mycheck)

    cur.close()

    b = sql
