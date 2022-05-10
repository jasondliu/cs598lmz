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
    return 1

def my_cb3(p):
    my_threading_local.a.close()
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.enable_shared_cache(True)
    sqlite3.threadsafety = 2
    sqlite3.config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
    sqlite3.set_authorizer(my_cb2)

    sqlite3.set_trace_callback(my_cb)
    sqlite3.set_trace_callback(my_cb3)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    a.execute("select test(1, 2)")

    print("done")

if __name__ == "
