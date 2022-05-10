import io
# Test io.RawIOBase.readinto

import _io
import _testcapi

class TestRawIO(io.RawIOBase):

    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def readinto(self, b):
        l = len(b)
        if self.pos + l > len(self.buf):
            l = len(self.buf) - self.pos
            b = memoryview(b)[:l]
        b[:] = self.buf[self.pos:self.pos+l]
        self.pos += l
        return l

    def readable(self):
        return True

class TestRawBufferedIO(TestRawIO, io.BufferedIOBase):
    pass


