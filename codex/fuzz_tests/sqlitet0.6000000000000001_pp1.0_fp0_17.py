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
    my_threading_local.a = None

def my_cb_thread(p):
    my_threading_local.a = None

def my_cb_lock(p):
    return

def my_cb_unlock(p):
    return

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_SERIALIZED), None)

sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MULTITHREAD), None)
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_SINGLETHREAD), None)

sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MULTITHREAD), None)

sqlite3.sqlite3_config
