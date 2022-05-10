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

def my_cb2(p):
    a = my_threading_local.a
    assert a.execute("select test(1, 2)").fetchone()[0] == 1

    return 1

sqlite3.sqlite3_config(SQLITE_CONFIG_MULTITHREAD)

my_cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
my_cb_ptr = my_cb_type(my_cb)
my_cb_ptr2 = my_cb_type(my_cb2)

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
lib.sqlite3_thread_cleanup()
lib.sqlite3_thread_init()

lib.sqlite3_create_disposable_module(sqlite3.sqlite_version_info, "test", None, None, my_cb_ptr, my_cb_ptr2)

con = sqlite3.connect(":memory:")
con.close()
