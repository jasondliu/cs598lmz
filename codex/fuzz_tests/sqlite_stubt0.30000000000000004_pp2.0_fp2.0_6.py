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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.db), 0x00000004, None)
sqlite3.sqlite3_busy_handler(my_threading_local.db, my_cb, None)

def my_thread():
    my_threading_local.a.execute("select test(1, 2)")

t = threading.Thread(target=my_thread)
t.start()
t.join()
</code>
The above code crashes with the following error:
<code>Exception ignored in: &lt;bound method deleting_conn.__del__ of &lt;sqlite3.Connection [closed] object at 0x7f6b7a6a2e58&gt;&gt;
Traceback (most recent call last):
  File "test.py", line 23, in __del__
  File "test.py", line 23, in __del__
  File "test.py", line 23, in __del__
  File "test.py", line 23
