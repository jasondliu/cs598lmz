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

def test_callback():
    p = ctypes.c_void_p(0)

    fn = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    sqlite3.enable_shared_cache(False)
    sqlite3.threadsafety = 1
    sqlite3.sqlite3_thread_cleanup()

    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)

    try:
        sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
    except:
        pass

    sqlite3.sqlite3_initialize()
    sqlite3.sqlite3_enable_shared_cache(False)
    sqlite3.create_function("test", 2, lambda a, b: a)
    sqlite3.sqlite3_shutdown()

    sqlite3.sqlite3_initialize()
    sqlite3.sqlite3_enable_shared_cache(False)
