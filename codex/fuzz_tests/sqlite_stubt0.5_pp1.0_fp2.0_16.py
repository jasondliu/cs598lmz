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
    # This should not segfault
    my_threading_local.a.execute("select test(1,2)")
    return 1

sqlite3.sqlite3_initialize()

try:
    sqlite3.sqlite3_shutdown()
except AttributeError:
    pass

sqlite3.sqlite3_initialize()

sqlite3.sqlite3_create_disposable_module("my_module", 0, my_cb, my_cb2, None, None)

sqlite3.sqlite3_dispose_module("my_module")

sqlite3.sqlite3_shutdown()
</code>

