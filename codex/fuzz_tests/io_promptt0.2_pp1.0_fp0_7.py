import io
# Test io.RawIOBase.readinto()

import _io

class MyRawIO(_io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        if self.pos + n > len(self.buf):
            n = len(self.buf) - self.pos
            b = memoryview(b)[:n]
        b[:] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def readable(self):
        return True

class MyBufferedIO(_io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        if self.pos + n > len(self.raw.buf):
            n = len(self.raw.buf) - self.pos
            b = memoryview(b)[:n]
        b[
