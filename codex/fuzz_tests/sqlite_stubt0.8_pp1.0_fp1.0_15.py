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

# create new thread with new _tstate
print("new thread, new _tstate")
print("new thread, new _tstate")
print("new thread, new _tstate")
t = threading.Thread(target=my_cb, args=(1,), name="my_thread")
t.daemon = True
t.start()
t.join()

my_threading_local.a.execute("SELECT test(1, 2)")

print("new thread, new _tstate")
print("new thread, new _tstate")
print("new thread, new _tstate")
t = threading.Thread(target=my_cb, args=(1,), name="my_thread")
t.daemon = True
t.start()
t.join()

# create new thread with new _tstate
print("new thread, same _tstate")
print("new thread, same _tstate")
print("new thread, same _tstate")
t = threading.Thread(target=my_cb, args=(1,), name="my_thread")
t.
