import io
# Test io.RawIOBase

import unittest
from test import support
from io import BytesIO, BufferedIOBase, UnsupportedOperation

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Issue #11459: check that RawIOBase is an ABC
        self.assertRaises(TypeError, io.RawIOBase)
        self.assertRaises(TypeError, io.RawIOBase, None)

    def test_read(self):
        rawio = io.RawIOBase()
        self.assertRaises(UnsupportedOperation, rawio.read)
        self.assertRaises(UnsupportedOperation, rawio.read, 0)

    def test_readall(self):
        rawio = io.RawIOBase()
        self.assertRaises(UnsupportedOperation, rawio.readall)

    def test_readinto(self):
        rawio = io.RawIOBase()
        b = bytearray(10)
        self.assertRaises(UnsupportedOperation, rawio.readinto, b)

    def test
