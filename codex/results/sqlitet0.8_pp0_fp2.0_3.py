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

del_flag = False

def my_del_cb():
    global del_flag
    del_flag = True
    a = my_threading_local.a
    if a is not None:
        a.execute("select test(1, 2)")

def run_test():
    expect = True

    libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

    p = ctypes.POINTER(ctypes.c_int)()

    # Register the callback
    libsqlite3.sqlite3_test_control(1, my_cb, p)

    del_flag = False
    # Run the callback
    libsqlite3.sqlite3_test_control(2, my_del_cb, None)

    if del_flag != expect:
        return 0
    else:
        return 1

run_test()
</code>
The above code crashes on the line <code>my_threading_local.a.execute("select test(1, 2)")</code>, because
