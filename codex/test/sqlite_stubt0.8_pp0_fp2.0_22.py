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

p = ctypes.POINTER(ctypes.c_int)()

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(p))
lib.sqlite3_set_authorizer(p[0], my_cb, 0)

a = sqlite3.connect(DB_URI, uri=True)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

def get_thread_id():
    return id(my_threading_local)

a.create_function("my_func", 0, get_thread_id)

# this line is the point of the whole test: while a thread is inside
# sqlite3_open, it will call the authorizer callback. That callback
# ends by setting a variable in thread-local storage.
#
# So, this query ends up running the
