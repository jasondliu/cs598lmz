import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase

class TestRawIO(RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        b[:3] = b"foo"
        return 3

    def write(self, b):
        pass

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertEqual(RawIOBase.seekable.__objclass__, RawIOBase)
        self.assertEqual(RawIOBase.readable.__objclass__, RawIOBase)
        self.assertEqual(RawIOBase.writable.__objclass__, RawIOBase)
        self.assertEqual(RawIOBase.read.__objclass__, RawIOBase)
        self.assertEqual(RawIOBase.readinto.__objclass__, RawIOBase)
        self.assertEqual(RawIO
