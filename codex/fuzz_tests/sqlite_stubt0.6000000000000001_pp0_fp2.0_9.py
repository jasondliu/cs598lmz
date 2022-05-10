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

def my_cb2(p):
    b = my_threading_local.a

    return 1

def main():
    try:
        sqlite3.enable_callback_tracebacks(True)
    except AttributeError:
        print("sqlite3.enable_callback_tracebacks not available")

    sqlite3.set_authorizer(my_cb)

    conn = sqlite3.connect(DB_URI, uri=True)
    c = conn.cursor()

    c.execute("select test(1,2)")
    c.execute("select test(1,2)")

    sqlite3.set_authorizer(my_cb2)

    conn.close()

if __name__ == '__main__':
    main()
</code>
This code results in the following traceback which is only since the change in commit 5c5d7b5:
<code>Traceback (most recent call last):
  File "./test_sqlite3.py", line 44, in &lt;module&gt;
    main()
 
