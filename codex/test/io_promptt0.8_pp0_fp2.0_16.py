import io
# Test io.RawIOBase as base class for RawIOBase test class
try:
    io.RawIOBase
except AttributeError:
    RawIOBase = object
else:
    RawIOBase = io.RawIOBase

class MyRawIO(RawIOBase):

    def __init__(self, value):
        self.value = value
        self.pos = 0
        self.closed = False

    def readall(self):
        return (self.value * len(self.value)).encode("latin-1")

    def readinto(self, b):
        data = self.readall()
        b[:len(data)] = data
        return len(data)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = len(self.value) + pos
