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

sqlite3.enable_shared_cache(True)
sqlite3.set_authorizer(my_cb)

conn = sqlite3.connect(DB_URI, uri=True)
conn.execute("select test(?)", (1,))
conn.execute("select test(?)", (2,))
conn.execute("select test(?)", (3,))
conn.execute("select test(?)", (4,))
conn.execute("select test(?)", (5,))
conn.execute("select test(?)", (6,))
conn.execute("select test(?)", (7,))
conn.execute("select test(?)", (8,))
conn.execute("select test(?)", (9,))
conn.execute("select test(?)", (10,))
