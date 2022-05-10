import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def __init__(self):
        self.pos = 0
        self.buf = b'abcdefghijklmnopqrstuvwxyz'

    def readinto(self, b):
        n = len(b)
        if self.pos >= len(self.buf):
            return 0
        if self.pos + n > len(self.buf):
            n = len(self.buf) - self.pos
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def write(self, b):
        n = len(b)
        if self.pos + n > len(self.buf):
            n = len(self.buf) - self.pos
        self.buf = self.buf[:self.pos] + b[:n] + self.buf[self.pos+n:]
        self.pos += n
        return n

    def seek(self, pos, whence=0
