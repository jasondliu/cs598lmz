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


sqlite3.enable_callback_tracebacks(True)
sqlite3.sqlite3_auto_extension(None)
sqlite3.sqlite3_auto_extension(my_cb)

def my_exec(conn, sql):
    conn.execute(sql)

for i in range(10000):
    t = threading.Thread(target=my_exec, args=(sqlite3.connect(DB_URI, uri=True), "SELECT test(1, 2)"))
    t.start()
    t.join()
</code>
At about the 1000th iteration, the program crashes with the following error:
<code>Exception ignored in: &lt;function my_cb at 0x7f5f2fceb158&gt;
Traceback (most recent call last):
  File "pysqlite_callback.py", line 23, in my_cb
  File "/usr/lib/python3.6/sqlite3/__init__.py", line 515, in create_function
    self.connection.create_function(name, num_
