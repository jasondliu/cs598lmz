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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_vfs_register(ctypes.c_void_p(sqlite3.sqlite3_vfs_find("unix-none")), 0)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)
try:
    sqlite3.connect(DB_URI, uri=True)
except:
    pass
a = my_threading_local.a

def test_functions_are_not_leaked():
    a = sqlite3.connect(DB_URI, uri=True)
    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    assert any(t.dlerror is None for t in threading.enumerate()
               if t is not threading.current_thread()),\
               "leaking function objects"
