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

view[0] = ord('x')

# Check that the file object is closed when the buffer object is deleted.
# This is important, since the buffer object owns the file object's
# reference to the raw object.

import weakref

class Raw(object):
    def __init__(self):
        self.closed = False
    def close(self):
        self.closed = True
    def fileno(self):
        return 42

r = Raw()
f = io.BufferedReader(r)
wr = weakref.ref(r)
del f
gc.collect()
assert wr() is None or wr().closed
