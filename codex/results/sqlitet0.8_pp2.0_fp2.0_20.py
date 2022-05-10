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

    return 1;

# I believe the original purpose was to test whether the following
# pattern would crash the interpreter:
#
#     class Deleting:
#         def __del__(self):
#             import threading
#             threading.Thread(target=lambda: Deleting()).start()
#
#     Deleting()

def register_my_cb():
    global my_cb_id

    assert my_cb_id is None
    my_cb_id = sqlite3.set_authorizer(my_cb)

def unregister_my_cb():
    global my_cb_id

    assert my_cb_id is not None
    sqlite3.set_authorizer(None)
    my_cb_id = None


def run_thread():
    register_my_cb()
    unregister_my_cb()
    register_my_cb()
    unregister_my_cb()

def main():
    global my_cb_id

    my_cb_id = None
    t = threading.Thread(target=run_thread)
    t.
