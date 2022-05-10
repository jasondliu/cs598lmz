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

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(3, my_cb)
sqlite3.sqlite3_initialize()

a = sqlite3.connect(DB_URI, uri=True)

a.close()
del a

del my_threading_local

import gc
gc.collect()
</code>
If you run it, at the <code>a.close()</code> line you'll get
<code>Fatal Python error: unexpected exception during garbage collection
Traceback (most recent call last):
  File "C:\Program Files\Python38\lib\multiprocessing\popen_spawn_win32.py", line 124, in do_pipe_connection
    hpipe, _ = self._connect(pipe_name)
OSError: [WinError 6] The handle is invalid

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Program Files\Python38\lib\multiprocessing\connection.py", line
