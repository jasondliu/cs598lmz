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

rbx = ctypes.cdll.LoadLibrary(ctypes.util.find_library("rubinius"))
rbx.rbx_init()

rbx.rbx_register_func("do_stuff", my_cb, 0)

class Foo:
    def test(self, a, b):
        return "foo" + str(a) + str(b)

    def test_before_sqlite3(self):
        return "foo"

FOO = ctypes.cast(ctypes.pointer(Foo()), ctypes.c_void_p).value
rbx.rbx_register_func("Foo.test", FOO, 0)
rbx.rbx_register_func("Foo.test_before_sqlite3", FOO, 0)
