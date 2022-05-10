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

my_cb_pointer = ctypes.cast(ctypes.CFUNCTYPE(ctypes.c_int)(my_cb),
                            ctypes.c_void_p).value

# Run the test
sqlite3.sqlite3_thread_cleanup()
sqlite3.sqlite3_thread_set_callback(my_cb_pointer)
thread1 = threading.Thread(target=lambda: 1)
thread2 = threading.Thread(target=lambda: 1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
sqlite3.sqlite3_thread_cleanup()
