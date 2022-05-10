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
    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    sqlite3.sqlite3_progress_handler(my_threading_local.a.connection, 1, cb, None)

    t = threading.Thread(target=sqlite3.connect, args=(DB_URI,), kwargs={"uri": True, "factory": deleting_conn})
    t.start()
    t.join()

    print("Finished")

if __name__ == "__main__":
    main()
</code>
If I run this script, I get the following output:
<code>Finished
Exception ignored in: &lt;bound method deleting_conn.__del__ of &lt;__main__.deleting_conn object at 0x7f0f8c24b9b0&gt;&gt;
Traceback (most recent call last):
  File "/home/user/test.py", line 22, in __del__
  File "/usr
