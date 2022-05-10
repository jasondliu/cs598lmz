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

@contextlib.contextmanager
def deleted_p(p):
    try:
        yield
    finally:
        # NB: this is a leaked resource!
        # it works when deleting p in thread itself,
        # but fails on any other thread
        # del p
        pass

def mine(p):
    with deleted_p(p):
        threading.Thread(target=p.c_thread).start()

def main():
    p = ctypes.c_void_p()
    p.thread_create = ctypes.CFUNCTYPE(None, ctypes.c_void_p)(mine)
    p.c_thread = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    p.thread_create(p)
</code>
And when we e.g run it and delete the p in thread itself:
<code>thread_local_02$ python main.py
thread_local_02$
</code>
But when we comment del p in my inner function, it does
