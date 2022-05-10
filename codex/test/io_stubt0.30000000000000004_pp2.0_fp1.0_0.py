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

# Issue #10338: check that the buffer is not freed before the
# BufferedReader is.

import weakref

class File(io.RawIOBase):
    def readinto(self, buf):
        pass
    def readable(self):
        return True

f = io.BufferedReader(File())
buf = f.read(1)
