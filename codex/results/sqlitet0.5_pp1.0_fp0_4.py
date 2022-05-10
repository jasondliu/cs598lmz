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

ctypes.pythonapi.PyEval_InitThreads()

sqlite3.enable_callback_tracebacks(True)

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, 0, None)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_initialize()

sqlite3.sqlite3_create_function(
    None, b"test", 2, sqlite3.SQLITE_UTF8, None, my_cb, None, None
)

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db))
sqlite3.sqlite3_exec(my_threading_local.db, b"SELECT test(1, 2);", None, None, None)
sqlite3.sqlite3_
