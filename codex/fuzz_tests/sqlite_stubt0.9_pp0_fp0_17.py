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

def test():
    lib = ctypes.util.find_library('sqlite3')
    if not lib:
        return

    ctx = 0
    res = ctypes.CDLL(lib).sqlite3_test_control(-3, 3, ctypes.c_void_p(ctx), my_cb, None)
    assert res == 0

    with sqlite3.connect(":memory:") as b:
        with pytest.raises(sqlite3.DatabaseError) as exc_info:
            b.execute("SELECT test(1, 2)").fetchall()
        assert "no such function: test" in exc_info.value.args[0]

    my_threading_local.a.close()
    del my_threading_local.__dict__["a"]
</code>

