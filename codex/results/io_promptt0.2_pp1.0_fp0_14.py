import io
# Test io.RawIOBase

import unittest
from test import support
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRWPair

class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')

    def test_close(self):
        io.RawIOBase().close()

    def test_detach(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().detach)

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().seek, 0)

    def test_tell(self):
        self.assertRaises(
