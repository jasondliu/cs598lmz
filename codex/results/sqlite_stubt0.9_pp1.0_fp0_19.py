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

sqlite3.sqlite3_open(ctypes.byref(ctypes.c_int()), ":memory:")
sqlite3.sqlite3_progress_handler(my_threading_local.a.connection.cursor().connection, 100, ctypes.CFUNCTYPE(ctypes.c_int)(my_cb), ctypes.c_void_p())

c = my_threading_local.a.cursor()
c.execute("select test(1, 2);")  # ok

del my_threading_local.a

c.execute("select test(1, 2);")  # Exception: segfault
</code>


A:

The reason the <code>sqlite3_progress_handler()</code> function is needed is to give sqlite a chance to check for interrupts from other threads. Applications can call <code>sqlite3_interrupt()</code> to tell the database handle to cause any current and subsequent running SQL statements to abort as quickly as possible. Only one can call <code>sqlite3_interrupt()</code>
