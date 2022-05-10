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

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_initialize()

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
lib.sqlite3_threadsafe.restype = ctypes.c_int

assert lib.sqlite3_threadsafe() == 1

sqlite3.sqlite3_enable_shared_cache(True)

sqlite3.threadsafety = 1
sqlite3.sqlite_version_info = (3, 6, 23, 1)
sqlite3.sqlite_version = "3.6.23.1"

sqlite3.create_function("test", 2, my_cb)

a = sqlite3.connect(DB_URI, uri=True)

# This will cause the bug
a.cursor().execute("select test()").fetchall()

a.close()

# This will cause the error
my_thread
