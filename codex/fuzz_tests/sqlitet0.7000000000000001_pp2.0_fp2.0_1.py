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

@pytest.mark.parametrize("db_uri", [DB_URI, ":memory:"])
def test_thread_local(db_uri):
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    libc.pthread_create(ctypes.c_void_p(), None, cb, None)
    libc.pthread_join(ctypes.c_long(), None)

    a = sqlite3.connect(db_uri, uri=True, factory=deleting_conn)
    with a:
        assert a.execute("SELECT test(1, 2);").fetchone() == (1,)
        my_threading_local.a.execute("SELECT test(1, 2);")
