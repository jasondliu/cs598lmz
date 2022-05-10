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

ctypes.pythonapi.PyThreadState_SetAsyncExc(
    ctypes.c_long(threading.get_ident()),
    ctypes.py_object(KeyboardInterrupt))

try:
    for i in range(100):
        t = threading.Thread(target=my_cb, args=(i,))
        t.start()
except:
    pass
</code>
Any ideas?


A:

If it were my code I would use a <code>threading.local()</code> object instead of a <code>threading.Thread</code> subclass to store the connection object.
I would also use the <code>with</code> statement to ensure that the connection is closed when finished.
<code>import sqlite3
import threading

DB_URI = "file:test?mode=memory"

def my_cb(p):
    with sqlite3.connect(DB_URI, uri=True) as a:
        def test_fn(a, b):
            return a

        a.create_function("test", 2,
