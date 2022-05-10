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

    return 101

sqlite3.sqlite3_enable_shared_cache(1)
libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
if libc.pthread_create(ctypes.c_void_p(), None, my_cb, None):
    raise ctypes.get_errno()

a = deleting_conn("test")
c = a.cursor()
c.execute("select test(11, 22)")
c.execute("select * from sqlite_master")
b = my_threading_local.a
del my_threading_local.a
c.execute("select test(33, 44)")
b.close()
print(a.execute("select test(11, 22)").fetchall())
print(a.execute("select * from sqlite_master").fetchall())
print(a.execute("select test(33, 44)").fetchall())
a.close()
