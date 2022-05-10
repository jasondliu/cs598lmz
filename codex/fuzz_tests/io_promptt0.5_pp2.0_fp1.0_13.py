import io
# Test io.RawIOBase

import io
import unittest
from test import support

class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read, 10)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto, memoryview(bytearray(10)))

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, memoryview(b''))

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)

    @support.
