import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# A mixin for testing RawIOBase methods.
class RawIOMixin:

    # Subclasses must define self.myfile, self.mode, and self.closed_msg.

    def test_read(self):
        self.assertEqual(self.myfile.read(0), b'')
        self.assertEqual(self.myfile.read(5), b'hello')
        self.assertEqual(self.myfile.read(1), b'')
        self.assertEqual(self.myfile.read(1), b'')
        self.assertRaises(ValueError, self.myfile.read, -1)
        self.assertRaises(TypeError, self.myfile.read, None)
        self.assertRaises(TypeError, self.myfile.read, 'foo')
        self.assertRaises(TypeError, self.myfile.read, 1.5)
        self.assertRaises(TypeError, self.myfile.read
