import io
# Test io.RawIOBase

import _io
import unittest

import test.support

class RawIOBaseTest(unittest.TestCase):

    def test_rawiobase(self):
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase))
        self.assertEqual(io.RawIOBase.read, _io.IOBase.read)
        self.assertEqual(io.RawIOBase.readinto, _io.IOBase.readinto)
        self.assertEqual(io.RawIOBase.write, _io.IOBase.write)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().read)
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().read, 0)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation,
