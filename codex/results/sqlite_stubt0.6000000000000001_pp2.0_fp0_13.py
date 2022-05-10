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
    ctypes.pythonapi.PyEval_InitThreads()
    ctypes.pythonapi.PyEval_AcquireThread(ctypes.c_void_p())

    sqlite3.enable_callback_tracebacks(True)

    db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    db.create_function("my_cb", 0, my_cb)

    db.execute("select my_cb()")

    print(my_threading_local.a.execute("select test(?, ?)", ("test", "test")).fetchone())

test()
</code>
I have found out that the memory leak only occurs when the <code>sqlite3.enable_callback_tracebacks(True)</code> function has been called.
I have also found out that the memory leak occurs only if the callback function creates a new connection and then creates a function within that connection.
The memory leak does not occur if the callback function creates a function in the connection which called the callback function.
The memory leak does not occur if the
