import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support

# A mixin for testing RawIOBase objects.
class RawIOMixin:

    # Subclasses should override.
    def new_io(self):
        raise NotImplementedError

    def test_read(self):
        io = self.new_io()
        self.assertRaises(TypeError, io.read)
        self.assertRaises(TypeError, io.read, 'x')
        self.assertRaises(TypeError, io.read, None)
        self.assertRaises(ValueError, io.read, -1)
        self.assertRaises(ValueError, io.read, sys.maxsize+1)
        self.assertEqual(io.read(0), b'')

    def test_readinto(self):
        io = self.new_io()
        b = bytearray(b'x' * 10)
        self.assertRaises(TypeError, io.readinto)
        self.assertRaises(TypeError,
