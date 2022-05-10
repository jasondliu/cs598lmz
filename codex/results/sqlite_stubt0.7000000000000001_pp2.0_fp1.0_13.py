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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open(DB_URI.encode(), ctypes.byref(ctypes.c_void_p()))
lib.sqlite3_set_authorizer(None, my_cb, None)

threads = [threading.Thread() for i in range(1000)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("OK")
</code>
The script crashes with
<code>Exception ignored in: &lt;function _close_socket.&lt;locals&gt;._close_socket at 0x7fcfc7b0f840&gt;
Traceback (most recent call last):
  File "/usr/lib/python3.6/socket.py", line 589, in _close_socket
    _socket.close(skt)
OSError: [Errno 9] Bad file descriptor
</code>
when I try to close the connection. If I remove the <
