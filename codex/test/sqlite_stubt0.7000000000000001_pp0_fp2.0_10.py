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

def my_cb2(p, argc, argv, col_names):
    if col_names:
        col_names = sqlite3.SQLITE_STATIC
    else:
        col_names = sqlite3.SQLITE_TRANSIENT

    sqlite3.result_text(p, "foo", 3, sqlite3.SQLITE_TRANSIENT)
    sqlite3.result_text(p, "foo", 3, sqlite3.SQLITE_TRANSIENT)
    sqlite3.result_text(p, "foo", 3, sqlite3.SQLITE_TRANSIENT)
    sqlite3.result_text(p, "foo", 3, sqlite3.SQLITE_TRANSIENT)
    sqlite3.result_text(p, "foo", 3, sqlite3.SQLITE_TRANSIENT)

    return 1

def my_cb3(p, argc, argv, col_names):
    if col_names:
        col_names = sqlite3.SQLITE_STATIC

