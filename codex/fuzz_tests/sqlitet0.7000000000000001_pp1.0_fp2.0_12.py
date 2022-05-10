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
    sqlite3.sqlite3_ssl_init(ctypes.util.find_library('sqlite3'), 0, None, None)

    sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.db),
                            sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_URI,
                            None)

    sqlite3.sqlite3_create_function_v2(my_threading_local.db, "test", 2,
                                       sqlite3.SQLITE_UTF8 | sqlite3.SQLITE_DETERMINISTIC,
                                       ctypes.c_void_p(0),
                                       test_fn, None, None, None)

    c = sqlite3.Cursor(my_threading_local.db)

    c.execute("SELECT test(test(?, ?), ?)", ("hello", "world", "!"))

    print(c.
