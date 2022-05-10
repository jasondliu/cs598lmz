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
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(1), ctypes.py_object(SystemError))
    ctypes.pythonapi.PyEval_ReInitThreads()
    ctypes.pythonapi.PyEval_ReleaseThread(ctypes.pythonapi.PyThreadState_Get())
    ctypes.pythonapi.PyEval_AcquireThread(ctypes.pythonapi.PyThreadState_Get())

    sqlite3.enable_callback_tracebacks(True)

    t = threading.Thread(target=my_cb, args=(1,))
    t.start()
    t.join()

    print my_threading_local.a

if __name__ == "__main__":
    main()
</code>
This is a slightly modified version of the example provided by the sqlite3 module documentation.
When the above is run, the following error is produced:
<code>Process finished with exit code -1073741819 (0xC0000005)
</code>
The error is produced in the <
