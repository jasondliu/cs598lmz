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
    del my_threading_local.a

def test_close_thread_local_file_descriptor():
    ctypes.CDLL(ctypes.util.find_library('c')).atexit(1, None)
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.enable_shared_cache(True)
    sqlite3.threadsafety = 1
    sqlite3.cache.enable()
    sqlite3.register_adapter(int, lambda x: x)
    sqlite3.connect(DB_URI, uri=True).close()
    sqlite3.threadsafety = 2
    sqlite3.cache.enable()
    sqlite3.register_adapter(int, lambda x: x)
    sqlite3.connect(DB_URI, uri=True).close()
    sqlite3.threadsafety = 3
    sqlite3.cache.enable()
    sqlite3.register_adapter(int,
