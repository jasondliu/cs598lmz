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
    my_threading_local.a.close()

    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
    lib.sqlite3_initialize()

    lib.sqlite3_enable_shared_cache(1)

    lib.sqlite3_thread_cleanup()

    lib.sqlite3_create_function_v2(
        0, b"my_cb", 0, sqlite3.SQLITE_UTF8, 0, my_cb, 0, 0, 0)
    lib.sqlite3_create_function_v2(
        0, b"my_cb2", 0, sqlite3.SQLITE_UTF8, 0, my_cb2, 0, 0, 0)

    conn = sqlite3.connect(DB_URI, uri=True)

