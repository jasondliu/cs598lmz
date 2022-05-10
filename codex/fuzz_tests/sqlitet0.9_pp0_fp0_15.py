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

lib = ctypes.CDLL(ctypes.util.find_library("curl"))
lib.curl_global_init.argtypes = [ctypes.c_long]
lib.curl_global_init(0)

libcurl = lib.curl_easy_init()
my_cb_func = ctypes.CFUNCTION(ctypes.c_int, ctypes.py_object)(my_cb)
op_result = lib.curl_easy_setopt(libcurl, 10157, ctypes.addressof(my_cb_func))
assert(op_result == 0)

op_result = lib.curl_easy_perform(libcurl)
assert(op_result == 0)

del my_threading_local
lib.curl_easy_cleanup(libcurl)
lib.curl_global_cleanup()
</code>

