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

def do_Python_call(p):
    a = my_threading_local.a
    a.execute("select test(1, 2)")
    return 1

def my_test():
    p = sqlite3.load_extension("my_hook", "my_test_hook")

sqlite3.register_adapter(bool, int)

try:
    my_test()
except Exception as e:
    print(e)
