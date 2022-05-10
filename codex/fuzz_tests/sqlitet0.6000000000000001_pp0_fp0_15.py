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

def test_func():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.conn = conn
    cursor = conn.cursor()
    cursor.execute("create table t(x)")
    cursor.execute("select test(x, x) from t")
    cursor.close()
    conn.close()

test_func()

# This should not segfault
my_threading_local.conn = None
my_threading_local.a = None

print "ok"
