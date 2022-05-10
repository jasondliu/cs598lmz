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

sqlite3.sqlite3_initialize()

c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

c.execute("CREATE TABLE abc (a TEXT, b TEXT)")

c.set_authorizer(my_cb)

c.execute("INSERT INTO abc VALUES ('test', 'test')")

print my_threading_local.a

sqlite3.sqlite3_shutdown()
</code>
If I make the <code>a</code> connection global, the <code>a</code> connection closes normally.
<code>import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    global a
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def
