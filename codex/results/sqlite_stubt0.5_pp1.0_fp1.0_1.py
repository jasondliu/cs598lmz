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

    if a is None:
        return 1
    else:
        return 0

def my_cb3(p):
    a = my_threading_local.a

    if a is None:
        return 1
    else:
        return 0

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)

    lib.sqlite3_config(lib.SQLITE_CONFIG_URI, 1)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.close()

    lib.sqlite3_initialize()

    lib.sqlite3_config(lib.SQLITE_CONFIG_SINGLETHREAD)

    lib.sqlite3_config(lib.SQLITE_CONFIG_MULTITHREAD)

    lib.sqlite3_config(lib.SQLITE_CON
