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

def main():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.enable_shared_cache(True)
    sqlite3.set_authorizer(my_cb)

    sqlite3.connect(DB_URI, uri=True)
    sqlite3.connect(DB_URI, uri=True)

    print("done")

if __name__ == '__main__':
    main()
</code>
I'm using Python 3.6.1 and sqlite 3.16.2.
The above code results in the following error:
<code>Exception ignored in: &lt;bound method deleting_conn.__del__ of &lt;sqlite3.Connection object at 0x7f7b1c0d9f30&gt;&gt;
Traceback (most recent call last):
  File "/usr/lib/python3.6/sqlite3/__init__.py", line 523, in __del__
  File "/usr/lib/python3.6/sqlite3/__init__.py", line 473
