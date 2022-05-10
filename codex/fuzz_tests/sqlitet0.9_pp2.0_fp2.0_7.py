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

drivername = ctypes.util.find_library('sqlite3')
if not drivername:
    raise Exception("Can't find libsqlite3")

sqlite3.sqlite3_enable_shared_cache(True)

# bad: dlopen() should not be used to open shared libraries such as
# libsqlite3.
ctypes.CDLL(drivername).sqlite3_auto_extension(my_cb)

a = sqlite3.connect(DB_URI, uri=True)
a.set_progress_handler(my_cb, 5)

# bad: extending the connection is unsafe
my_threading_local.a.create_function("test", 2, test_fn)
