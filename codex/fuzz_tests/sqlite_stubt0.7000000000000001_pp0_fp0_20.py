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

libc = ctypes.CDLL(ctypes.util.find_library("c"))

libc.setenv("SQLITE_DEBUG", "1", 1)
libc.setenv("SQLITE_USE_URI", "1", 1)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn, check_same_thread=False)
conn.create_function("test", 1, my_cb)
conn.execute("select test(?)", (1,))
conn.close()

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn, check_same_thread=False)
conn.execute("select test(?)", (2,))
conn.close()
