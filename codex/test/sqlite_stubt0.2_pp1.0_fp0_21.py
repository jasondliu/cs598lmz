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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.db), 0x00000002, None)
sqlite3.sqlite3_busy_handler(my_threading_local.db, my_cb, None)

def test_fn(a, b):
    return a

my_threading_local.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
my_threading_local.a.create_function("test", 2, test_fn)

my_threading_local.a.execute("create table test(a, b)")
my_threading_local.a.execute("insert into test(a, b) values (1, 2)")
my_threading_local.a.execute("insert into test(a, b) values (3, 4)")
my_threading_local.a.execute("insert into test(a, b) values (5, 6)")

