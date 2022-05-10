import io
# Test io.RawIOBase

import _io
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
            def readinto(self, buf):
                n = min(len(buf), len(self.buf) - self.pos)
                buf[:n] = self.buf[self.pos:self.pos+n]
                self.pos += n
                return n
            def readable(self):
                return True
        buf = bytearray(b"abcdefghi")
        f = TestRawIO(buf)
        self.assertEqual(f.read(0), b"")
        self.assertEqual(f.read(5), b"abcde")
        self.assertEqual(f.read(5), b"fghi")
        self.assertE
