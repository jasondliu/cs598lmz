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


def my_cb2(a, p):
    rv = 0
    try:
        rv = my_threading_local.a.execute("select test(1, 2)").fetchone()[0]
    except:
        print(sys.exc_info())
    return rv

def my_cb3(a):
    my_threading_local.a.close()
    del my_threading_local.a
    return 5

def my_cb4(a, b):
    return 1

def my_cb5(a, b):
    return 1

sqlite3.enable_callback_tracebacks(True)
sqlite3.set_trace_callback(my_cb)
sqlite3.complete_statement("select func(1)")
sqlite3.set_authorizer(my_cb2, 1)
sqlite3.complete_statement("select func(1)")
sqlite3.set_progress_handler(my_cb3, 2)
sqlite3.complete_statement("select func(1)")
sqlite
