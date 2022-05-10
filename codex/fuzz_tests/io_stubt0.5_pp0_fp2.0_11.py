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

import gc
gc.collect()

print(view)
</code>
This prints <code>bytearray(b'\xd0\x1f\x93\x8c\x00\x00\x00\x00')</code>.
So it seems the <code>io.BufferedReader</code> is not released correctly, and the buffer is kept alive by a cycle.

This is a bug in Python.

