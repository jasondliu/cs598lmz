import io
# Test io.RawIOBase

import io
import unittest

from test import support

class RawIOTest(unittest.TestCase):
    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)

    def test_isatty(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().isatty)

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().seek, 0)

    def test_tell(self):
        self.assertRaises(io
