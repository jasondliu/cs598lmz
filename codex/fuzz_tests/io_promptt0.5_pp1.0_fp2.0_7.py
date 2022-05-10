import io
# Test io.RawIOBase

import unittest
import io
from test import test_support


class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readall)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b"x")

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().seek, 0)

    def test_tell(self):
        self.assertRaises(io
