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

def test():
    try:
        lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    except OSError:
        raise unittest.SkipTest("sqlite3 not available")

    lib.sqlite3_config(ctypes.c_int(2), ctypes.c_int(1))

    lib.sqlite3_enable_shared_cache(ctypes.c_int(1))

    sqlite3.sqlite_version_info
    sqlite3.sqlite_version
    sqlite3.threadsafety
    sqlite3.paramstyle
    sqlite3.complete_statement("select 1;")

    sqlite3.register_adapter(int, lambda x: x)
    sqlite3.register_adapter(str, lambda x: x)
    sqlite3.register_adapter(float, lambda x: x)
    sqlite3.register_adapter(buffer, lambda x: x)
    sqlite3.register_adapter(unicode, lambda x: x)

    sqlite3
