import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

f = io.BufferedReader(File())
f.read(1)
del f
</code>
It segfaults:
<code>$ python3 test.py 
Segmentation fault
</code>
So it seems that the <code>readinto</code> method is called twice on the same <code>File</code> object.
Is this a bug in the <code>io</code> module?


A:

It seems that the <code>io</code> module is not thread-safe.
To fix the problem, I had to make my <code>File</code> class thread-safe. Here is a working example:
<code>import io
import threading

class File(io.RawIOBase):
    def __init__(self):
        self.lock = threading.Lock()
    def readinto(self, buf):
        with self.lock:
            global view
            view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

f =
