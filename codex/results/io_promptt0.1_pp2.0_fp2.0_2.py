import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().readinto, b'')

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().write, b'')

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().fileno)

    def test_isatty(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().isatty)

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().seek, 0)

    def test_tell(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().tell)

    def
