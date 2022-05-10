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
    a = my_threading_local.a
    a.close()
    my_threading_local.a = None

    return 1

sqlite3.sqlite3_enable_shared_cache(1)

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_config(ctypes.c_int(7), ctypes.c_int(1))

libsqlite3.sqlite3_initialize()

libsqlite3.sqlite3_config(ctypes.c_int(5), my_cb, my_cb2)

libsqlite3.sqlite3_shutdown()
</code>

