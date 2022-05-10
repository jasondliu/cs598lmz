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
    a = my_threading_local.a
    a.execute("select test(1, 2)")
    return 1

sqlite3.sqlite3_shutdown()

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

lib.sqlite3_config(5, my_cb, "")

lib.sqlite3_initialize()

lib.sqlite3_config(6, my_cb2, "")

lib.sqlite3_shutdown()
</code>
If I run this example, I get the following error:
<code>Exception ignored in: &lt;bound method Connection.__del__ of &lt;__main__.deleting_conn object at 0x7f0c1b9f15c0&gt;&gt;
Traceback (most recent call last):
  File "test.py", line 25, in __del__
  File "test.py", line 17, in close
sqlite3.ProgrammingError:
