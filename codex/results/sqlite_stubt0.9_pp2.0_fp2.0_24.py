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

    return 15

def main():
    path = ctypes.util.find_library("sqlite3")
    if path is None:
        raise Exception("unable to find sqlite3")

    lib = ctypes.CDLL(path)

    lib.sqlite3_enable_shared_cache(1)
    sqlite3.enable_shared_cache(1)

    if sqlite3.threadsafety != 2:
        raise Exception("threadsafety!=2!")

    if lib.sqlite3_initialize() != 0:
        raise Exception("sqlite3_initiliaze failed")

    lib.sqlite3_enable_shared_cache(1)
    sqlite3.enable_shared_cache(1)

    if sqlite3.threadsafety != 2:
        raise Exception("threadsafety!=2 after sqlite3_initialize!")

    sqlite3._threadsafety = 1

    if sqlite3.threadsafety != 1:
        raise Exception("threadsafety!=1!")

    if sqlite3.sqlite_version_info != lib.sqlite3_libversion_
