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
    b = my_threading_local.a

    b.execute("select test(2, 3)")
    assert b.execute("select test(2, 3)").fetchone() == (2, )

    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_shared_cache(1)

# This has to be done to avoid a segfault in python's sqlite3 module
# when it is unloaded
ctypes.pythonapi.Py_MakePendingCalls()

t1 = threading.Thread(target=my_cb, args=(1, ))
t2 = threading.Thread(target=my_cb2, args=(1, ))

t1.start()
t2.start()

t1.join()
t2.join()
