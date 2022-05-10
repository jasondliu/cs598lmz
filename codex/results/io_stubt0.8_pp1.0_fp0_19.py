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
print(view)
</code>

As a workaround to the above, I have tried implementing a class that inherits both from <code>io.RawIOBase</code> and <code>io.BufferedIOBase</code>, with a custom <code>readinto</code> method that delegates to the <code>base</code> <code>readinto</code> method, which itself should delegate to the <code>_read_buffered</code> method in <code>io.BufferedIOBase</code>. Doing so yields a <code>NotImplementedError</code> on the call to <code>_read_buffered</code>:
<code>#!/usr/bin/env python3

import io

class File(io.RawIOBase, io.BufferedIOBase):
    def readinto(self, buf):
        return self.base.readinto(buf)
    def readable(self):
        return True
    def _read_buffered(self):
        return self.base._read_buffered()

f = File()
f.read(1)
del f

