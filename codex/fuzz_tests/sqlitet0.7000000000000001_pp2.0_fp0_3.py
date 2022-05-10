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

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.sqlite3_threadsafe()

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_threadsafe()

libsqlite3.sqlite3_thread_cleanup()

sqlite3.sqlite_version_info

old_tb = sqlite3.threadsafety
sqlite3.threadsafety = 2

try:
    sqlite3.threadsafety = 3
except ValueError:
    pass
except:
    raise

sqlite3.threadsafety = old_tb

old_tb = sqlite3.threadsafety
sqlite3.threadsafety = 2

sqlite3.sqlite_version_info

libsqlite3.sqlite3_thread_cleanup()

my_threading_local.a = None

libsqlite3.sqlite3_thread_cleanup()

libsqlite3.sqlite3_thread_clean
