import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import errno
import _io

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
        self.assertEqual(io.RawIOBase().isatty(), False)

    def test_close(self):
        # A RawIOBase implementation is not required to do anything in close(),
        # but it must exist.
        io.RawIOBase().close()

    def
