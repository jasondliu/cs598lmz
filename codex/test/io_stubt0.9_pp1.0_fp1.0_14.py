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

# Exercise the probing path for a file flush. This may or
# may not be done by File.__dealloc__, and Python 2 may
# or may not grab a hold of the file object with a weakref.
import _testcapi
