import io
# Test io.RawIOBase.readinto()

import _io

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf

    def readinto(self, b):
        n = len(self.buf)
        if n > len(b):
            n = len(b)
        b[:n] = self.buf[:n]
        self.buf = self.buf[n:]
        return n

    def readable(self):
        return True

class TestBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw

    def readinto(self, b):
        return self.raw.readinto(b)

    def readable(self):
        return True

class TestRawIOWrapper(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.readbuf = b''

    def readinto(self, b):
        n = len(b)
        m = len(self.read
