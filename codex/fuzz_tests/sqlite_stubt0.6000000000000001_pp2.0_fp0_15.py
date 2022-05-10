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

try:
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
except:
    print("SKIP")
    raise SystemExit

lib.sqlite3_config(1, 1) # SQLITE_CONFIG_MULTITHREAD
lib.sqlite3_config(2, 1) # SQLITE_CONFIG_MEMSTATUS
lib.sqlite3_config(3, 1) # SQLITE_CONFIG_MUTEX
lib.sqlite3_config(4, 0) # SQLITE_CONFIG_GETMUTEX
lib.sqlite3_config(5, 1) # SQLITE_CONFIG_LOOKASIDE
lib.sqlite3_config(6, 1) # SQLITE_CONFIG_LOG
lib.sqlite3_config(7, 1) # SQLITE_CONFIG_URI
lib.sqlite3_config(8, 1) # SQLITE_CONFIG_MEMDB
