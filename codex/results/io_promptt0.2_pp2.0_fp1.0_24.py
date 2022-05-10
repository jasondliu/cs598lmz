import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase, UnsupportedOperation

class TestRawIOBase(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(RawIOBase, 'mode'))
        self.assertTrue(hasattr(RawIOBase, 'name'))

    def test_abstract(self):
        self.assertRaises(TypeError, RawIOBase)

    def test_read(self):
        self.assertRaises(UnsupportedOperation, RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(UnsupportedOperation, RawIOBase().readinto, bytearray())

    def test_readall(self):
        self.assertRaises(UnsupportedOperation, RawIOBase().readall)

    def test_write(self):
        self.assertRaises(UnsupportedOperation, RawIOBase().write, b'')

    def test_fileno(self):
        self.assertRaises(UnsupportedOperation, RawIOBase().fil
