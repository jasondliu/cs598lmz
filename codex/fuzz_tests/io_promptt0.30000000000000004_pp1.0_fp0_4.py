import io
# Test io.RawIOBase.readinto()

import _io

class MyRawIO(_io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0
    def readinto(self, b):
        n = len(b)
        if self.pos >= len(self.buf):
            return 0
        if self.pos + n > len(self.buf):
            n = len(self.buf) - self.pos
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n
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

buf = b'abcdefghijklmnopqrstuvwxyz'

for n in range(
