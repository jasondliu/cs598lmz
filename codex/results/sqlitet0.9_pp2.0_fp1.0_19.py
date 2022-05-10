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
    if hasattr(my_threading_local, 'a'):
        assert my_threading_local.a != None, "connection is None"
        b = my_threading_local.a
    else:
        b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        my_threading_local.b = b
    b.execute("select test(1, 2)")
    return 1

def calc_sizeof(val, depth=-1):
    if depth == 0:
        return
    size = sys.getsizeof(val)
    if isinstance(val, collections.Set):
        return size + sum(calc_sizeof(x, depth=depth-1) for x in val)
    if isinstance(val, collections.Mapping):
        for k in val:
            size += calc_sizeof(k, depth=depth-1) + calc_sizeof(val[k], depth=depth-1)
            return size
    if hasattr
