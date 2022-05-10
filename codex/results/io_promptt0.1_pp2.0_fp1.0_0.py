import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().readinto, bytearray())

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().readall)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().write, b'')

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().fileno)

    def test_is
