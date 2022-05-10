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

def try_run():
    my_threading_local.a.execute("select test(?);", (10,))
    for row in my_threading_local.a.execute("select test(?);", (10,)):
        pass

my_cb(None)
try_run()

try_run()

try:
    try_run()
except AttributeError:
    raise Exception("A")
except sqlite3.ProgrammingError:
    pass
except:
    raise Exception("B")
</code>
Basically, I'm attempting to call a callback in Python, which creates a connection to a SQLITE database. Then, the callback is supposed to store the connection in a thread-local variable, and then my program is supposed to be able to use that connection.
However, this program only works the first time. The second time it is run, the statement <code>my_threading_local.a.execute("select test(?);", (10,))</code> raises an exception, saying that there is no such attribute <code>a</code>. I thought this was because the connection is
