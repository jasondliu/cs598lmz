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

clib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))
cb = sqlite3.sqlite3_callback(my_cb)

clib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.conn_ptr), 1, None)
assert isinstance(my_threading_local.conn_ptr.value, sqlite3.Connection)
clib.sqlite3_busy_handler(my_threading_local.conn_ptr, cb, 0)

del my_threading_local.a

cursor = my_threading_local.conn_ptr.execute("select test(1,2)")
assert next(cursor)[0] == 1

my_threading_local.conn_ptr.execute("create table test (a text)")

my_threading_local.conn_ptr.execute("insert into test values (?)", ("test",))

cursor = my_threading_local.conn_ptr.execute
