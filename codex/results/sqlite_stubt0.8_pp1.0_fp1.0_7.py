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

def my_collator(a, b):
    if not isinstance(a, str):
        a = str(a)
    if not isinstance(b, str):
        b = str(b)
    return -1 if a < b else (0 if a == b else 1)

def my_progress(count):
    if not hasattr(my_threading_local, "a"):
        return 0
    a = my_threading_local.a
    a.create_function("conn_test", 1, lambda x: x)
    a.execute("select conn_test(?)", (count,))
    return count == 5

def my_trace(stmt):
    if not hasattr(my_threading_local, "a"):
        return
    a = my_threading_local.a
    a.create_function("trace_test", 1, lambda x: x)
    a.execute("select trace_test(?)", (stmt,))

def my_authorizer(action, arg1, arg2, dbname):
   
