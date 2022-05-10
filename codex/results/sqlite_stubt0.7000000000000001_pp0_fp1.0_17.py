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
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)
print(sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb))

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("select test(1, 2)")
del a

a = my_threading_local.a
b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
print(a.execute("select test(1, 2)").fetchall())
print(b.execute("select test(1, 2)").fetchall())

# initialize/finalize may be called multiple times
sqlite3.sqlite3_finalize(None)
sqlite3.sqlite3_initialize()
sqlite3
