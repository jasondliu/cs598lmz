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
    my_threading_local.a.close()
    del my_threading_local.a
    return 1

sqlite3.sqlite3_open(":memory:", ctypes.byref(my_threading_local.conn))
sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(my_threading_local.conn2),
                        sqlite3.SQLITE_OPEN_FULLMUTEX | sqlite3.SQLITE_OPEN_URI, None)

sqlite3.sqlite3_create_function(my_threading_local.conn, b"open_db", 0,
                                sqlite3.SQLITE_UTF8, None, my_cb, None, None)
sqlite3.sqlite3_create_function(my_threading_local.conn2, b"close_db", 0,
                                sqlite3.SQLITE_UTF8, None, my_cb2, None, None)

my_threading_local.conn_
