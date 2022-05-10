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
    # this test is not thread safe, but it is not supposed to be
    # it is just to test that the sqlite3 module is thread safe
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.create_function("my_cb", 1, my_cb)
    c.execute("select my_cb(?)", (1,))
    c.execute("select test(?, ?)", (1, 2))
    c.close()
    assert my_threading_local.a.execute("select test(?, ?)", (1, 2)).fetchone()[0] == 1

def test_sqlite_threading_2():
    # this test is not thread safe, but it is not supposed to be
    # it is just to test that the sqlite3 module is thread safe
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
