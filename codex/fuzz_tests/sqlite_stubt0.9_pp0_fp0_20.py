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

def main():
    libc_string = ctypes.util.find_library('c')
    libc = ctypes.CDLL(libc_string, use_errno=True)

    sqlite3.sqlite_syscall_ptr = libc.syscall

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.set_progress_handler(my_cb, 10)

    thread = threading.Thread(target=lambda: ctypes.util.find_library('z'),
                              name="progress-thread")
    thread.start()
    thread.join()

    assert my_threading_local.a is not None

# this line triggers an assertion failure!?!
main()
