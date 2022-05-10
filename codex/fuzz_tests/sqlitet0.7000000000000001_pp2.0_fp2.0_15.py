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

ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.a), 0x00000002, None)

ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_progress_handler(my_threading_local.a, 10, my_cb, 0)

my_threading_local.a.execute("create table test (name text)")

my_threading_local.a.execute("select test(1, 2)")

print(my_threading_local.a.fetchone()[0])
</code>

