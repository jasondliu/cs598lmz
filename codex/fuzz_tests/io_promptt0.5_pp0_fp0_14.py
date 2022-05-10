import io
# Test io.RawIOBase

import io
import _io
import unittest
import weakref

# A mixin for RawIOBase subclasses that aren't readonly.
class RawIOMixin:

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, bytearray(1))

    def test_readline(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readline)

    def test_readlines(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readlines)

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readall)

    def test_readable(self):
        self.assertFalse(self.io.readable())

    def test_seekable(self):
        self.assertFalse(self.io.seekable())

    def test_writable(self):
        self.assertTrue(self.io.writable())

    def test_fileno(self):

