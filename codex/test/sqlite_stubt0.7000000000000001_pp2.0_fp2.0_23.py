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

def my_cb_step(p):
    return 1

def my_cb_final(p):
    return 1

def my_cb_destroy(p):
    return 0

my_cb_p = ctypes.cast(my_cb, ctypes.c_void_p).value
my_cb_step_p = ctypes.cast(my_cb_step, ctypes.c_void_p).value
my_cb_final_p = ctypes.cast(my_cb_final, ctypes.c_void_p).value
my_cb_destroy_p = ctypes.cast(my_cb_destroy, ctypes.c_void_p).value

sqlite3.sqlite3_create_function_v2(
    my_threading_local.a.dbapi_connection, "my_cb", 0, 0, None,
    my_cb_p, my_cb_step_p, my_cb_final_p, my_cb_destroy_p)

