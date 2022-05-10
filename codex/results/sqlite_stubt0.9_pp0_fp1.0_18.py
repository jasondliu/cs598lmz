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


c_cb = sqlite3.sqlite3_threadsafe_callback(my_cb)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_initialize()

lib.sqlite3_thread_init()

lib.sqlite3_config(lib.SQLITE_CONFIG_URI, 1)
assert lib.sqlite3_config(lib.SQLITE_CONFIG_URI, 0) == lib.SQLITE_OK

lib.sqlite3_thread_set_callback(c_cb)

lib.sqlite3_thread_cleanup()
</code>

