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

def my_cb_deleter(p):
    del my_threading_local.a

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_GETMALLOC, ctypes.pythonapi.PyMem_Malloc, ctypes.pythonapi.PyMem_Free)

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SCRATCH, ctypes.c_void_p(1))
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_PAGECACHE, ctypes.c_void_p(1), 1, 1)

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, True)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, ctypes.CFUNCTYPE(None, ctypes.
