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

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
print(lib)
print(lib.sqlite3_config)
ret = lib.sqlite3_config(1, my_cb, None)

if sys.version_info[0] < 3:
    assert(hasattr(my_threading_local, 'a'))
    assert('my_threading_local' in repr(my_threading_local.a.execute("SELECT test(1, 2)")))
else:
    assert(not hasattr(my_threading_local, 'a'))
    # Python 3's pysqlite makes this too hard to test. all we can do is not segfault.
    #assert('my_threading_local' in repr(my_threading_local.a.execute("SELECT test(1, 2)")))
