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

sqlite3.sqlite3_busy_handler(my_cb, None)

class MyThread(threading.Thread):
    def __del__(self):
        self.join()

    def run(self):
        my_threading_local.a.cursor().execute("select test(1,2)")

for _ in xrange(100):
    t = MyThread()
    t.start()
</code>
This causes "a" to be garbage collected during the execution of the thread. I assume that it's a sqlite3 bug. Is there any workaround?


A:

<blockquote>
<p>I assume that it's a sqlite3 bug. Is there any workaround?</p>
</blockquote>
You assume incorrectly. You should really fire up gdb or lldb and debug the test case. You'll find that the database object (<code>sqlite3_connection</code>) is being garbage collected because you only hold a reference to it for the duration of the callback. Once the callback returns, your "a" variable is destroyed. To solve this, you need to hold
