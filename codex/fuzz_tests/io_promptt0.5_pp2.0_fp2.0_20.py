import io
# Test io.RawIOBase.readinto()

import unittest
from test import support

class TestRawIO(io.RawIOBase):

    def __init__(self, buf):
        self._buf = buf
        self._pos = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            self._pos = pos
        elif whence == 1:
            self._pos += pos
        elif whence == 2:
            self._pos = len(self._buf) + pos
        return self._pos

    def tell(self):
        return self._pos

    def readinto(self, b):
        n = len(b)
        if self._pos + n > len(self._buf):
            n = len(self._buf) - self._pos
            b = memoryview(b)[:n]
        b[:n] = self._buf[self._pos:self._pos+n]
        self._pos += n
        return n


class Read
