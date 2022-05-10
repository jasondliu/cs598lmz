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

sqlite3.sqlite3_log(my_cb)

db = sqlite3.connect(DB_URI, uri=True)

db.execute("select test(?)", (5,))

db.close()

print(my_threading_local.a.execute("select test(?)", (5,)).fetchall())

my_threading_local.a.close()
