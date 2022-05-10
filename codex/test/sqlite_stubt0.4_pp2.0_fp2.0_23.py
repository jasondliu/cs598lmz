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

sqlite3.enable_callback_tracebacks(True)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_vfs_register(sqlite3.sqlite3_vfs_find("unix-none"), 0)
sqlite3.sqlite3_create_function(None, "my_cb", 1, None, my_cb)

for i in range(0, 10):
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.create_function("test", 2, lambda a, b: a)
    conn.execute("select my_cb(1)")
    conn.close()

# This is the problem. The connection that was created by the callback
