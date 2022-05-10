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
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.current_thread().ident),
                                               ctypes.py_object(KeyboardInterrupt))

class MyThread(threading.Thread):
    def run(self):
        p = ctypes.c_void_p(0)
        sqlite3.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(p),
                                sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_URI,
                                None)
        sqlite3.sqlite3_create_function(p, b"test", 2, sqlite3.SQLITE_UTF8, None, my_cb, None, None)

        while True:
            time.sleep(1)

if __name__ == "__main__":
    t = MyThread()
    t.start()
    main()
