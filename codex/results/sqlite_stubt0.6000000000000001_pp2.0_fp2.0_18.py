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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("SQLite"))
lib.sqlite3_config(1, my_cb, None)

# Repeatedly open the same database to exercise the connection pool
for i in range(10):
    con = sqlite3.connect(DB_URI, uri=True)
    con.close()
    con = sqlite3.connect(DB_URI, uri=True)
    con.close()

# Repeatedly call the function to exercise the connection pool
for i in range(10):
    cur = my_threading_local.a.cursor()
    cur.execute("SELECT test(1, 2)")
    print(cur.fetchone())
    cur.close()
