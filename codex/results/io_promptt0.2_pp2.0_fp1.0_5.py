import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        # RawIOBase defines read, readinto, write, seek, tell, truncate
        # and close.
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, f.write, b'')
        self.assertRaises(io.UnsupportedOperation, f.seek, 0)
        self.assertRaises(io.UnsupportedOperation, f.tell)
        self.assertRaises(io.UnsupportedOperation, f.truncate)
        self.assertRaises(io.UnsupportedOperation, f.close)

    def test_readinto(self):
        # Test readinto
        f = io.BytesIO(b"1234567890")
