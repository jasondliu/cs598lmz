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

def my_cb_deleter(p):
    my_threading_local.a = None
    return 1

def test():
    n = 1
    sqlite3.enable_shared_cache(True)
    sqlite3.threadsafety = 1
    assert sqlite3.threadsafety == 1
    sqlite3.threadsafety = 0
    assert sqlite3.threadsafety == 0
    sqlite3.threadsafety = 1
    assert sqlite3.threadsafety == 1
    sqlite3.threadsafety = 2
    assert sqlite3.threadsafety == 2
    assert sqlite3.threadsafety == 2
    sqlite3.threadsafety = 0
    assert sqlite3.threadsafety == 0
    sqlite3.threadsafety = 1
    assert sqlite3.threadsafety == 1
    sqlite3.threadsafety = 2
    assert sqlite3.threadsafety == 2
    assert sqlite3.threadsafety == 2

    sqlite3.threadsafety = n
    if n == 0:
        sqlite3.threadsafety = 1
    else:
       
