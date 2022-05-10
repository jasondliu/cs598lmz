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

sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), 1)

l = ctypes.util.find_library("sqlite3")

p = ctypes.CDLL(l)

p.sqlite3_thread_cleanup()

cb = sqlite3.sqlite_api.threading_cb(my_cb)

assert sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_SINGLETHREAD), cb) == sqlite3.SQLITE_OK

p.sqlite3_thread_cleanup()

# cb(None)
