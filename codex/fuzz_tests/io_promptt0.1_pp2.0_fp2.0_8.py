import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'),
                        "RawIOBase is missing the 'mode' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'name'),
                        "RawIOBase is missing the 'name' attribute")

    def test_abc(self):
        self.assertTrue(io.RawIOBase.readinto(bytearray(1)) is None,
                        "RawIOBase.readinto() should return None")
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.read)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.readline)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.readlines)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.write, b'')
        self
