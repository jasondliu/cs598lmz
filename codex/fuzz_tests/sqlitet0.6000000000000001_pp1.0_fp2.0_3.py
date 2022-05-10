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

def my_thread(n):
    for i in range(n):
        ctypes.pythonapi.PyGILState_Ensure()
        ctypes.pythonapi.PyGILState_Release(ctypes.c_long(0))

# Install the callback
sqlite3.sqlite3_set_authorizer(my_cb, 0)

# Create a thread that will release and reacquire the GIL
t = threading.Thread(target=my_thread, args=(100,))
t.start()

# Open the database, which will invoke the callback
a = sqlite3.connect(DB_URI, uri=True)

# Wait for the thread to finish
t.join()

# This will crash (when built with -O0)
a.execute("select test(1, 2)")
</code>

