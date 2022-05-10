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

lib = ctypes.util.find_library("sqlite3")
if lib is None:
    raise Exception("sqlite3 shared library not found")

lib = ctypes.CDLL(lib)

lib.sqlite3_enable_shared_cache(1)

cb = sqlite3.set_authorizer(my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.execute("create table test (a, b)")
a.execute("insert into test values (1, 2)")
a.execute("insert into test values (3, 4)")

print(a.execute("select test(a, b) from test").fetchall())

a.execute("create table test2 (a, b)")
a.execute("insert into test2 values (1, 2)")
a.execute("insert into test2 values (3, 4)")

print(a.execute("select test(a, b) from test2
