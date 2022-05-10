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

# Don't crash
str(view)

# Issue #12531: unowned ndarray object should not expose __array_interface__
import numpy.core.multiarray
a = numpy.core.multiarray.scalar(1)
try:
    a.__array_interface__
except AttributeError:
    pass
