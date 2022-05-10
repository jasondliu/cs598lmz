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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.b),
                        2 | 0x00800000, ctypes.c_char_p(None))


# install callback to create a connection for each thread
sqlite3.sqlite3_thread_init(my_threading_local.b)
sqlite3.sqlite3_create_function(my_threading_local.b, "my_cb", 0, 1, None, my_cb)
sqlite3.sqlite3_set_authorizer(my_threading_local.b, my_cb, None)
sqlite3.sqlite3_set_trace_callback(my_threading_local.b, my_cb, None)
sqlite3.sqlite3_set_profile(my_threading_local.b, my_cb, None)

def thread_fn():
    my_threading_local.a.execute("select my_cb(?)", (1,))
    my_threading_local.a.
