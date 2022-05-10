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

def my_cb_2(p):
    a = my_threading_local.a
    a.execute("SELECT test(?, ?)", (1, 2))
    return 1

def test_create_function():
    # Create a new database and register a callback
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.create_function("test", 1, my_cb)

    # Execute the callback in a new thread
    t = threading.Thread(target=lambda: a.execute("SELECT test(?)", (1,)))
    t.start()
    t.join()

    # Verify that the callback was executed
    assert my_threading_local.a is not None

def test_create_function_with_thread_local():
    # Create a new database and register a callback
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.create_function("test_2", 1, my_cb_2)

    #
