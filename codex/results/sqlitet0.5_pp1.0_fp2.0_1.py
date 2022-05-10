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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)

# The following is a workaround for http://bugs.python.org/issue18456
# If you are on a platform where you can't use the workaround,
# you can still use the test suite, but it may crash and leave
# a .db-wal file in the current directory.
sqlite3.sqlite3_vfs_register(sqlite3.sqlite3_vfs_find("unix"), 1)

# a is created by my_cb, and should be destroyed by the garbage
# collector, but that doesn't happen because of the reference
# cycle created by the traceback.
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local
