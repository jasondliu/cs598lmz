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

sqlite3.sqlite3_set_authorizer(my_cb)

conn = sqlite3.connect(DB_URI, uri=True)
my_threading_local.a.close()
</code>
The code above will raise a <code>sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.</code>
The problem is that the <code>sqlite3_set_authorizer</code> callback is executed in the main thread, but the <code>sqlite3.connect</code> call is executed in the new thread. It would seem that the sqlite3 module creates the connection in the main thread, and then passes it to the new thread, which is not allowed.
How can I make sqlite3 create the connection in the new thread? Is there a way to specify the <code>threading.local</code> object to use when creating the connection?


A:

I ended up using the <code>threading.local</code> object in the callback, and then calling an other function in the new thread to get the connection from the threading
