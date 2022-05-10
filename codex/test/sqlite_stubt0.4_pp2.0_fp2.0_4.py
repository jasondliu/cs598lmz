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

def test_cb(p):
    return 1

def my_cb_final(p):
    my_threading_local.a.close()
    return 1

def test_cb_final(p):
    return 1

def my_cb_enter(p):
    return 1

def test_cb_enter(p):
    return 1

def my_cb_leave(p):
    return 1

def test_cb_leave(p):
    return 1

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_initialize()
