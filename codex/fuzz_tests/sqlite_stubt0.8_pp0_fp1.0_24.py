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

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(1)
sqlite3.sqlite3_config(2, 1)
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(3, my_cb)

a = sqlite3.connect(":memory:")
b = sqlite3.connect(DB_URI, uri=True)

assert b.connection == my_threading_local.a.connection

# The following code crashes the second time it runs under valgrind 3.2.1
# (but not the first time). It looks like memory is leaked, but I haven't
# been able to track that down yet.
c = sqlite3.connect(DB_URI, uri=True)
del c
del b
del a
c = sqlite3.connect(DB_URI, uri=True)
del c
