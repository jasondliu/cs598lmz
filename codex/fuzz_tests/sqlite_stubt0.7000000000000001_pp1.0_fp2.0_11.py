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

def test_func():
    ctypes.pythonapi.Py_AddPendingCall(my_cb, None)

test_func()

my_threading_local.a.execute('SELECT test(1, 2)').fetchall()
</code>

Here's the failure:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/home/user/.virtualenvs/venv/lib/python3.5/sqlite3/dbapi2.py", line 723, in execute
    return self.cursor.execute(statement, parameters)
sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 2, and there are 1 supplied.
</code>


A:

I think this is a problem with sqlite3 itself. It doesn't correctly handle parameters passed through a callback.
I have a workaround, though. I found a create_function method that accepts keyword arguments, and I can pass my parameters in that way.
<code>import
