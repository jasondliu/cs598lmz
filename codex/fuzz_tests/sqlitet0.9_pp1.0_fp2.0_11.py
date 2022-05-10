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

p = ctypes.create_string_buffer(ctypes.util.find_library("sqlite3"),
    my_cb)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
conn.create_function("p", 0, p)

for i in xrange(1):
    conn.execute("select p()").fetchall()

conn.close()
