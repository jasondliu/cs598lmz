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

# If a previous call to sqlite3_shutdown is not followed by a call to
# sqlite3_initialize, then most operations on the sqlite3_value
# objects do not operate as expected and their results are undefined.
# http://www.sqlite.org/c3ref/vtab_config.html
sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MULTITHREAD))
sqlite3.sqlite3_initialize()

sqlite3.sqlite3_uri_boolean(ctypes.c_int(-1), ctypes.c_int(-1))

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_SERIALIZED))
sqlite3.sqlite3_initialize()

sqlite3.sqlite3_threadsafe()

sqlite3.sqlite3_config(ctypes.c_int(
