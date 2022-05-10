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

def test_create_function():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    my_cb_p = lib.sqlite3_set_authorizer(my_cb, None)

    conn = sqlite3.connect(DB_URI, uri=True)

    # the bug was that this would deadlock for the first thread making a call
    x = conn.execute("select test(1, 2)").fetchone()[0]
    assert x == 1

    # now ensure that we can use the callback and SQLite to still work
    a = my_threading_local.a

    cursor = a.execute('select test(1, 2);')
    result = cursor.fetchone()[0]
    assert result == 1

    # cleanup
    my_cb_p = lib.sqlite3_set_authorizer(None, None)
