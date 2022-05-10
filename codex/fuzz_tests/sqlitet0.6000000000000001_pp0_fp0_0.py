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

def my_cb2(p):
    my_threading_local.a.execute("select test(1,2)")
    return 0

def my_cb3(p):
    my_threading_local.a.close()
    return 0

def my_cb4(p):
    return 0

sqlite3.enable_callback_tracebacks(True)

sqlite3.set_authorizer(my_cb, "test")

conn = sqlite3.connect(DB_URI, uri=True)
conn.execute("create table test (i int)")

sqlite3.set_authorizer(my_cb2, "test")

cur = conn.cursor()
cur.execute("insert into test values (1)")

sqlite3.set_authorizer(my_cb3, "test")

cur.execute("select * from test")

sqlite3.set_authorizer(my_cb4, "test")

cur.close()
conn.close()
