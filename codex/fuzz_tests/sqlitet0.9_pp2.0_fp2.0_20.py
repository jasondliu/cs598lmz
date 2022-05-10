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

sqlite3.set_trace_callback(my_cb)

a = sqlite3.connect(DB_URI, uri=True)

a.execute("delete from test")

# wait for callback thread
time.sleep(1)

ctypes.pythonapi.PyThreadState_Get = ctypes.PYFUNCTYPE(
    ctypes.py_object)(("PyThreadState_Get",
                      ctypes.util.find_library("python3.7m")))

thread_state = ctypes.pythonapi.PyThreadState_Get()

a = my_threading_local.a

a.execute("select test(?, ?)", (1, 0))

# check that we can use a connection on the callback thread
</code>
When I run it I get:
<code>sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 11560 and this is thread id 11556
</code>
So, it seems that the <code>sqlite3.Connection</code
