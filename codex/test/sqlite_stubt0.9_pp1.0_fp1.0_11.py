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

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

def f():
    a = sqlite3.connect(DB_URI, uri=True)
    a.create_collation("name", my_cb, None)
    assert 'a' in a.execute("SELECT test(1,2);").fetchone()

    a.execute("SELECT test(1,2) COLLATE name;").fetchone()
    assert 'a' in a.execute("SELECT test(1,2) COLLATE name;").fetchone()

lib = ctypes.util.find_library('sqlite3')
dll = ctypes.CDLL(lib)
dll.sqlite3_enable_shared_cache(1)

t1 = threading.Thread(target=f)
t2 = threading.Thread(target=f)

t1.start()
t2.start()

a = sqlite3.connect(DB_URI, uri=True)
thread1_conn
