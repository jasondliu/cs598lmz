import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref
import sys

# A mixin for RawIOBase subclasses that are not readonly
class RawIOBaseWriteTestsMixin:
    def test_write(self):
        self.assertEqual(self.io.write(b"blah"), 4)
        self.assertEqual(self.io.write(bytearray(b"blah")), 4)
        self.assertEqual(self.io.write(memoryview(b"blah")), 4)
        self.assertEqual(self.io.write(array.array('b', b"blah")), 4)
        self.assertRaises(TypeError, self.io.write, "blah")
        self.assertRaises(TypeError, self.io.write, u"blah")
        self.assertRaises(TypeError, self.io.write, "blah".encode("ascii"))
