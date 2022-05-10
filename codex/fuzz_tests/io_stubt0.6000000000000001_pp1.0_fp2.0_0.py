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
I've tried to use <code>gc.collect()</code> and <code>del f</code> but it doesn't work.
I also tried to make <code>view</code> a <code>ctypes</code> array and call <code>ctypes.memset(view, 0, len(view))</code>, but it doesn't help.
I'm using Python 3.5.2 on Linux 64bits.


A:

It seems to be working for me.
<code>import io
import gc
import ctypes
import os

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BuffearReader(File())
f.read(1)
del f

# do the memory test

gc.collect()

view_bytes = bytearray(len(view))
ctypes.memmove(ctypes.addressof(view_bytes), view, len(view))
print(view_bytes)

