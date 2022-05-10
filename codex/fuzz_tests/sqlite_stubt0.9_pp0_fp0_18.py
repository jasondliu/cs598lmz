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

def my_interrupt(t):
    # Workaround to get the current thread handle.
    thread_handle = ctypes.c_voidp.in_dll(
        ctypes.util.find_library("libpthread.so"),
        "_PyRuntime.gilstate.gil_thread.h")

    if t.handle is not None and t.handle == thread_handle.value:
        raise KeyboardInterrupt

# Define a new function to be used as the new sqlite3_interrupt handler since
# you can't get a reference to the external sqlite3 module from within the
# thread when this does get called.  I have disabled it for now as it is not
# contextually needed for this example.  But if you need it, then uncomment
# this and the following line (as well as the interrupt import above and the
# my_interrupt call below).
# sqlite3.api_func("in
