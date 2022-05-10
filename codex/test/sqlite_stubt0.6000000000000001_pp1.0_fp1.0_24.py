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
    return 1

def test_concurrent_access():
    # The testcase is to ensure that concurrent access to the sqlite3
    # library from different threads works without deadlocks.
    dll = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    dll.sqlite3_config(0x0004) # SQLITE_CONFIG_SINGLETHREAD
    dll.sqlite3_initialize()
    dll.sqlite3_config(0x0003) # SQLITE_CONFIG_SERIALIZED

    dll.sqlite3_enable_shared_cache(1)

    dll.sqlite3_enable_load_extension(1)
    dll.sqlite3_auto_extension(my_cb2)

    dll.sqlite3_auto_extension(my_cb)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

