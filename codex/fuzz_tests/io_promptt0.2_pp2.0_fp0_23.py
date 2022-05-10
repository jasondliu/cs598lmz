import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'))
        self.assertTrue(hasattr(io.RawIOBase, 'name'))

    def test_abc(self):
        self.assertTrue(io.RawIOBase.readinto(bytearray(1)) is None)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.read)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.readall)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.readline)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.readlines)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.write, b'')
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase.
