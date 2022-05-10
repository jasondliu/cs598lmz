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

def my_cb_final(p):
    my_threading_local.a.close()
    return 1

class MyError(Exception):
    pass

def my_cb_error(p):
    raise MyError()

class MyThread(threading.Thread):
    def run(self):
        c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

        c.create_function("test", 2, lambda a, b: a)

        c.execute("select test(1, 2)")

sqlite3.sqlite3_initialize()

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb_final)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb
