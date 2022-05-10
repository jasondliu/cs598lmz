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

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_db_config(sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1)
sqlite3.sqlite3_enable_load_extension(sqlite3.sqlite3_db_handle(my_cb), 1)

# We need to hold a reference to the connection otherwise it will be garbage
# collected and the destructor will be called.
conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

# We need to hold a reference to the function otherwise it will be garbage
# collected and the destructor will be called.
f = conn.create_function("test", 2, lambda a, b: a)

# If we don't do this, there will be a segfault on exit.
sqlite3.sqlite3_shutdown()
