import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import import_fresh_module

# The io module is not always available.
io = import_fresh_module('io', blocked=['_io'])


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

    def test_isatty(self):
        self.assertFalse(io.RawIOBase().isatty())

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)

    def
