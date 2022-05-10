import io
# Test io.RawIOBase.readinto()

import _io

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def readinto(self, b):
        n = len(self.buf) - self.pos
        if n > len(b):
            n = len(b)
        if n:
            b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

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
            self.pos = len(self.buf) + pos
        return self.pos

    def tell(self):
        return self.pos

class TestRawIO1(TestRawIO):
    def readinto(self, b):

