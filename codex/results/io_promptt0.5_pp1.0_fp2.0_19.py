import io
# Test io.RawIOBase

import _io

class TestRawIOBase(_io.RawIOBase):
    def __init__(self):
        self.pos = 0
    def read(self, n=-1):
        if self.pos >= 4:
            return b""
        n = min(n, 4-self.pos)
        self.pos += n
        return b"\x00" * n
    def seek(self, pos, whence=0):
        if whence == 1:
            pos += self.pos
        self.pos = pos
    def tell(self):
        return self.pos
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True

class TestRawIOBaseReadinto1(_io.RawIOBase):
    def readinto(self, b):
        b[:] = b"foo"
        return 3
    def readable(self):
        return True

class TestRawIOBaseReadinto2(_io.RawIOBase):
    def readinto(self, b):
       
