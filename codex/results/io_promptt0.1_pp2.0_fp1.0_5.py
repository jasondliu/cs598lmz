import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import bigaddrspacetest

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

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)

    def test_isatty(self):
        self.assertEqual(io.RawIOBase().isatty(), False)

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().
