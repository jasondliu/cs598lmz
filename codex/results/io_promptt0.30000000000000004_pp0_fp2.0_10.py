import io
# Test io.RawIOBase.readinto

import io
import unittest
import os

from test import support

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

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

    def readinto(self, b):
        l = len(b)
        if self.pos >= len(self.buf):
            return 0
        if self.pos + l > len(self.buf):
            l = len(self.buf) - self.pos
        b[:l] = self.buf[self.pos:self.pos+l]
        self.
