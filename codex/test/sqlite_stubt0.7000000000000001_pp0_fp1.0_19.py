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

# we need a non-NULL pointer, as sqlite3_set_authorizer() expects a pointer to a
# valid sqlite3*
sqlite3.sqlite_api.sqlite3_open(":memory:", ctypes.byref(ctypes.c_void_p(1)))
p = sqlite3.sqlite_api.sqlite3_uri_boolean(":memory:", "uri", 0)

# we need to keep a reference around, or the GIL will be released and the
# interpreter will crash
callback = sqlite3.sqlite_api.sqlite3_set_authorizer(1, my_cb, 0)

# make sure the authorizer callback is working
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

# we should be able to access the connection created inside the authorizer
# callback
