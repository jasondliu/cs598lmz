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

if __name__ == "__main__":
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.set_authorizer(my_cb)
    conn.execute("SELECT test(1, 2)")
</code>
I have tried this with other functions (such as <code>len</code>) and the <code>Deleter</code>s also happen with them.
I also tried adding to <code>PYTHONWARNINGS</code> with no success.
And, of course, my test case is a single-threaded test case. It's obviously unsafe to <code>return my_threading_local.a</code> from <code>my_cb</code> and so I do not expect sqlite to be able to use that connection in another thread, but I cannot see why the <code>Deleter</code> for the <code>a</code> variable in <code>my_cb</code> would be run on a different thread.
I've traced through <code>sqlite3_set_authorizer</code
