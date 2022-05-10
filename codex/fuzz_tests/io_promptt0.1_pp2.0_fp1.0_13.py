import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# A mixin for RawIOBase subclasses that aren't readonly.
class RawIOMixin:
    def test_readinto(self):
        self.assertRaises(TypeError, self.io.readinto, bytearray(b"0"))
        self.assertRaises(TypeError, self.io.readinto, memoryview(b"0"))
        self.assertRaises(TypeError, self.io.readinto, array.array('b', b"0"))

    def test_readall(self):
        self.assertRaises(TypeError, self.io.readall)

    def test_read(self):
        self.assertRaises(TypeError, self.io.read)

    def test_read1(self):
        self.assertRaises(TypeError, self.io.read1)

    def test_readline(self):
        self.assertRaises(TypeError, self.io.readline)

    def test_readlines(self
