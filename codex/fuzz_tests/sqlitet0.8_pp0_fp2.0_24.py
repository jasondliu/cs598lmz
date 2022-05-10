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

my_cb_t = sqlite3.sqlite3_set_authorizer(my_cb, ctypes.c_voidp())

def f():
    # This should be safe.
    test = my_threading_local.a

def g():
    # This can segfault.
    test = my_threading_local.a.cursor()
    test.close()

t1 = threading.Thread(target=f)
t2 = threading.Thread(target=g)
t1.start()
t2.start()
t1.join()
t2.join()
</code>

