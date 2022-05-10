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
    sqlite3.enable_callback_tracebacks(True)
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.get_ident()), ctypes.py_object(SystemError))

    p = sqlite3.prepare_v2(DB_URI, "select test(1, 2); select test(3, 4);", uri=True)
    callback = sqlite3.sqlite3_trace(p, my_cb)

    for (k,) in p.iterdump():
        print(k)

    a = my_threading_local.a
    print(a)

    callback.close()
    p.close()

main()
</code>
This is the output:
<code>select test(1, 2); select test(3, 4);
in test_fn
in test_fn
&lt;__main__.deleting_conn object at 0x7fddf6ff1e50&gt;
Exception AttributeError: "'NoneType' object has no attribute 'a
