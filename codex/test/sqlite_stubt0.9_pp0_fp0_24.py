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

def my_thread():
    s = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    s.execute('create table t (a, b)')
    s.commit()
    for a in xrange(10):
        s.execute('insert into t (a, b) values (?, ?)', (a, 'x'))
    s.execute('select * from t')

def main():
    conn = sqlite3.connect(":memory:")
    conn.create_function("my_cb", 0, my_cb)
    mod = ctypes.CDLL(ctypes.util.find_library("sqlite"))
    sqlite3.set_trace_callback(my_cb)
    mod.sqlite3_enable_shared_cache(1)
    sqlite3.set_authorizer(lambda a, b, c, d, e, f: False)
    sqlite3.enable_callback_tracebacks(True)
