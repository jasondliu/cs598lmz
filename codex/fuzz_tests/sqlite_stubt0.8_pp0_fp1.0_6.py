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

my_cb = sqlite3.sqlite3_set_authorizer(my_cb)

a = sqlite3.connect(DB_URI, uri=True)
b = a.execute("SELECT 1").fetchone()[0]
if b != 1:
    raise Exception("got %d, expected 1" % (b))

a.execute("ATTACH '%s' AS other" % (DB_URI))
b = a.execute("SELECT 1 FROM other.sqlite_master").fetchone()[0]
if b != 1:
    raise Exception("got %d, expected 1" % (b))
del b

a.execute("DETACH other")
del a

ctypes.pythonapi.Py_MakePendingCalls()

del my_threading_local.a
