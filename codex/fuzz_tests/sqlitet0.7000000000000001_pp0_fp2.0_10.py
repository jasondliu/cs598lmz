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

dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

# this should be unnecessary but it seems that sqlite3 doesn't call
# sqlite3_free() on the memory it gets from a SQLITE_TRANSIENT
# returned from a busy callback.
dll.sqlite3_free.argtypes = [ctypes.c_void_p]
dll.sqlite3_free.restype = None

c_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
db.set_authorizer(lambda *a, **kw: sqlite3.SQLITE_OK)
db.execute("create table test (a text)")
db.execute("insert into test values ('a'), ('b'), ('c')")
db.commit()

# causes the busy callback to be called with a SQLITE_BUSY result
db.execute("begin immediate")

