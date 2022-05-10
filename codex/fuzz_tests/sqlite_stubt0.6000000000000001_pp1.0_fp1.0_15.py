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

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

a.execute("create table test(a, b);")

a.execute("insert into test values(1, 2)")
a.execute("insert into test values(3, 4)")
a.execute("insert into test values(5, 6)")
a.execute("insert into test values(7, 8)")

a.execute("select test(a, b) from test;")

a.execute("select test(a, b) from test;")

a.execute("select test(a, b) from test;")

a.execute("select test(a, b) from test;")

a.execute("select test(a, b)
