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

def ru(db):
    pass

def crash():
    db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    db.create_function('my_cb', 1, my_cb)

    ru(db)

    ctypes.FunctionType(ctypes.c_void_p(), [])(0)

if __name__ == "__main__":
    crash()
</code>
The <code>deleting_conn</code> class is only necessary if your <code>sqlite3.connect()</code> invocation has <code>uri=True</code> and you are also using the <code>uri=True</code> keyword to other <code>sqlite3.connect()</code> calls you make inside the callback. The class causes the connection to be closed in the __del__() dunder method on exit (see https://docs.python.org/3/reference/datamodel.html#object.__del__).
In testing, with Python 3.6, this will give a segfault, usually on the <
