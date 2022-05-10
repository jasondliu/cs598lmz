import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(_io.RawIOBase):
            def __init__(self, buf):
                self.buf = buf
                self.pos = 0
            def readinto(self, b):
                n = len(b)
                if self.pos >= len(self.buf):
                    return None
                if n > len(self.buf) - self.pos:
                    n = len(self.buf) - self.pos
                b[:n] = self.buf[self.pos:self.pos+n]
                self.pos += n
                return n
        buf = b"abcdef"
        f = TestRawIO(buf)
        self.assertEqual(f.read(3), buf[:3])
        self.assertEqual(f.read(3), buf[3:6])
        self.
