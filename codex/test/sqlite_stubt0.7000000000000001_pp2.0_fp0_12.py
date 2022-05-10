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
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.a = a
    return 1

def test_thread_initialization():
    sqlite3.sqlite_initialize()
    sqlite3.sqlite_shutdown()
    sqlite3.sqlite_initialize()
    sqlite3.sqlite_shutdown()

    sqlite3.sqlite_open("test.db", 0, 0)
    sqlite3.sqlite_close()
    sqlite3.sqlite_open("test.db", 0, 0)
    sqlite3.sqlite_close()

def test_threading_init():
    try:
        sqlite3.enable_shared_cache(True)
    except AttributeError:
        # not supported
        return
    sqlite3.threadsafety = 2
    sqlite3.sqlite_initialize()
    sqlite3.set_authorizer(my_cb, None)
   
