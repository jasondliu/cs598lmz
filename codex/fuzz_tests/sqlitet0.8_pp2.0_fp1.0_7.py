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

if __name__ == "__main__":
    sqlite3.load_extension("./blah", "my_cb")
    t1 = threading.Thread(target=lambda: sqlite3.connect(DB_URI, uri=True, factory=deleting_conn))
    t2 = threading.Thread(target=lambda: sqlite3.connect(DB_URI, uri=True, factory=deleting_conn))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
</code>
This fails to load the extension, with the following output:
<code>Traceback (most recent call last):
  File "./__main__.py", line 34, in &lt;module&gt;
    t1.start()
  File "/usr/lib/python2.7/threading.py", line 736, in start
    self.run()
  File "/usr/lib/python2.7/threading.py", line 696, in run
    self.__target(*
