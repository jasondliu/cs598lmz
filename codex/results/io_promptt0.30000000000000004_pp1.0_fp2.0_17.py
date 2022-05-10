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
        return 0
    def write(self, b):
        return 0

class RawIOTest(unittest.TestCase):
    def test_attributes(self):
        self.assertEqual(RawIOBase.closed, False)
        self.assertEqual(RawIOBase.mode, None)
        self.assertEqual(RawIOBase.name, None)
        self.assertEqual(RawIOBase.newlines, None)
        self.assertEqual(RawIOBase.encoding, None)
        self.assertEqual(RawIOBase.errors, None)
        self.assertEqual(RawIOBase.line_buffering, False)

    def test_ioerror(self):
        self.assertRaises(IOError, Raw
