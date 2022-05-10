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

sqlite3.sqlite3_create_function(
    ctypes.c_void_p(ctypes.pythonapi.PyThreadState_GetDict()),
    b'test', 1, ctypes.c_void_p(my_cb))
threading.Thread(target=lambda: print(test(1,1))).start()
</code>
test.db:
<code>CREATE TABLE t (x); INSERT INTO t (x) VALUES (---); SELECT test(x) from t;
</code>
Then run with:
<code>python3 test.py &lt; test.db &amp;&amp; sleep 1; ps auxw
</code>
<code>CALL</code> doesn't work, so there is no way to free the resources.

