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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(0)

lib.sqlite3_enable_shared_cache(1)

lib.sqlite3_config(5, my_cb)

a = sqlite3.connect(DB_URI)

a.execute("create table test(foo text)")

b = sqlite3.connect(DB_URI, check_same_thread=False)

b.execute("insert into test(foo) values(?)", ("test",))

c = sqlite3.connect(DB_URI, check_same_thread=False)

c.execute("insert into test(foo) values(?)", ("test",))

d = sqlite3.connect(DB_URI, check_same_thread=False)

d.execute("select test(foo, ?) from test", ("test",))
