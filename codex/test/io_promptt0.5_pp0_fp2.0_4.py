import io
# Test io.RawIOBase.readinto()

import _io

# Issue #17051: io.RawIOBase.readinto() should call the readinto()
# method of its underlying raw stream.
class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf

    def readinto(self, b):
        n = len(b)
        if n > len(self.buf):
            n = len(self.buf)
        b[:n] = self.buf[:n]
        self.buf = self.buf[n:]
        return n

    def readable(self):
        return True

class TestRawBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw

    def readinto(self, b):
        return self.raw.readinto(b)

    def readable(self):
        return True

class TestBufferedReader(io.BufferedReader):
    def __init__(self, raw):
        io.BufferedReader.__init
