import io
# Test io.RawIOBase
import io
import sys

class TestRawIO(io.RawIOBase):
    def __init__(self, buf=b''):
        self.buf = buf

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            newpos = pos
        elif whence == 1:
            newpos = self.tell() + pos
        elif whence == 2:
            newpos = len(self.buf) + pos
        else:
            raise ValueError('whence must be 0, 1 or 2')
        if newpos < 0:
            raise ValueError('new position must be >= 0')
        self.pos = newpos

    def tell(self):
        return self.pos

    def readinto(self, b):
        n = len(self.buf) - self.pos
        if n < 0:
            n = 0
