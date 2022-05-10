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

if __name__ == '__main__':
    sqlite3.sqlite3_enable_shared_cache(1)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)
    sqlite3.sqlite3_initialize()
    sqlite3.sqlite3_thread_cleanup()

    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_thread_cleanup()

    sqlite3.sqlite3_open(DB_URI, ctypes.byref(ctypes.c_void_p()))
    sqlite3.sqlite3_thread_cleanup()

    lib.sqlite3_thread_cleanup()

    sqlite3.sqlite3_create_function(
        ctypes.byref(ctypes.c_void_p()),
        b"test",
        2,
        ctypes.c_void_p(),
        ctypes.c_void_p(),
        ctypes.c_void_
