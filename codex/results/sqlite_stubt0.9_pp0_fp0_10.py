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

def assert_function_is_loaded(conn):
    assert str(conn.execute("test('test', 'test')").fetchone()[0]) == "test"

if __name__ == "__main__":
    libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))
    fn = libc.fork
    fn.restype = ctypes.c_int
    fn.argtypes = [ctypes.CFUNCTYPE(ctypes.c_int), ctypes.c_int]

    first_assert = threading.Event()
    second_assert = threading.Event()
    third_assert = threading.Event()

    @ctypes.CFUNCTYPE(ctypes.c_int)
    def f():
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        assert_function_is_loaded(a)
        first_assert.set()

        second_assert.wait()
        assert_function_is_loaded(a)


