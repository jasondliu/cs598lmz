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

def test_func():
    sqlite3.sqlite3_open(":memory:", ctypes.byref(my_threading_local.db))
    sqlite3.sqlite3_create_function_v2(my_threading_local.db, b"test", 2, 1, None, my_cb, None, None, None)
    sqlite3.sqlite3_enable_shared_cache(1)

    my_threading_local.c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.c.executemany("insert into test values (?, ?)", [(1, "1"), (2, "2"), (3, "3")])

    my_threading_local.c.create_function("test", 1, lambda x: x)
    my_threading_local.c.create_aggregate("test", 1, lambda: None, lambda x, y: x)

    my_threading_local.c.execute("select test(test(test(test(
