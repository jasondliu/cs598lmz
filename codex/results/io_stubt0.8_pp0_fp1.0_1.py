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
</code>
Yet it (obviously?) raises a RuntimeError:
<blockquote>
<pre>RuntimeError: Exception while compiling:
  File "...", line 10, in readinto
    view = buf
UserWarning: Modifying a buffered object while in read mode will not work
</pre>
So what is the right way to pass a buffer transparently to another function?


A:

This is the right way to do it:
<code>import io
from ctypes import byref

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = byref(buf) # deep copy
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
</code>

