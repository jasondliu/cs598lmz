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


my_cb_p = sqlite3.progress_callback(my_cb, 10)

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

lib.sqlite3_exec(ctypes.c_void_p(), "CREATE TABLE test (a,b)",
                 ctypes.c_void_p(), ctypes.c_void_p(), ctypes.c_void_p())
lib.sqlite3_exec(ctypes.c_void_p(), "INSERT INTO test VALUES ('abc', 'def')",
                 ctypes.c_void_p(), ctypes.c_void_p(), ctypes.c_void_p())
e = []
def err_cb(data, err_code, err_msg):
    print err_message, err_code
    e.append((err_code, err_msg))
err_cb_p = sqlite3.error_callback(err_cb)
lib.sqlite3_exec(ctypes.c_void_p(),
                 "SELECT test('abc') FROM
