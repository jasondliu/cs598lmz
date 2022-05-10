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

    return 100, SQLITE_OK

sqlite3.enable_callback_tracebacks(True)

orig_init = sqlite3.api_init

def new_init(*args, **kwds):
    orig_init(*args, **kwds)
    sqlite3.sqlite3_auto_extension(my_cb)

sqlite3.api_init = new_init

sqlite3.sqlite3_threadsafe()

sqlite3.connect(DB_URI, uri=True).execute("SELECT test(1,2)")

sqlite3.sqlite3_auto_extension(None)
