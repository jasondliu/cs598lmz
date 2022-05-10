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

class Dummy(object):
    pass

my_callback = Dummy()
my_callback.xCallback = myCallbackType(my_cb)
my_callback.pArg = 0

r = sqlite3.startup(my_callback)

my_threading_local.a.cursor().execute("create table test (y string)")

# Reference count seems to be ok.
print(sys.getrefcount(my_threading_local.a))
print(sys.getrefcount(my_threading_loca
