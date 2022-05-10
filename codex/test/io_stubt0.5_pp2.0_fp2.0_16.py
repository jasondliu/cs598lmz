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

# The File object is still alive, but it's no longer referenced
# anywhere.  It should be collected.  If it is collected, then the
# memory pointed to by view should be freed.  So, if we create a new
# object that takes that memory, and it doesn't crash, then we're
# good.

class X(object):
    def __init__(self, buf):
        self.buf = buf

X(view)
