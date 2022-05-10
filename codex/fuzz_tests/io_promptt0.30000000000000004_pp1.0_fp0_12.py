import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    # File-like object that returns a given sequence of bytes
    class BytesIO(io.RawIOBase):
        def __init__(self, buf=b''):
            self.buf = buf
            self.offset = 0

        def readable(self):
            return True

        def writable(self):
            return True

        def seekable(self):
            return True

        def readinto(self, b):
            l = len(b)
            if self.offset >= len(self.buf):
                return None
            if self.offset + l > len(self.buf):
                l = len(self.buf) - self.offset
            b[:l] = self.buf[self.offset:self.offset + l]
            self.offset += l
            return l

        def write(self, b):
            self.buf += b
            return len(b)

        def seek(self, offset, whence
