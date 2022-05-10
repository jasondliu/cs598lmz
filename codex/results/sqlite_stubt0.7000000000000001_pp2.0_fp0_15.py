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

def my_cb_close(p):
    my_threading_local.a.close()

    return 1

def test_threaded_db():
    # Make sure the test is runnable in parallel
    sqlite3.enable_shared_cache(False)

    sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(p_sqlite3),
                            sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE,
                            None)
    sqlite3.sqlite3_create_function(p_sqlite3, b"my_cb", 0,
                                    sqlite3.SQLITE_UTF8, None, my_cb, None, None)
    sqlite3.sqlite3_create_function(p_sqlite3, b"my_cb_close", 0,
                                    sqlite3.SQLITE_UTF8, None, my_cb_close, None, None)

    assert sqlite3.sqlite3_exec(p_sqlite3
