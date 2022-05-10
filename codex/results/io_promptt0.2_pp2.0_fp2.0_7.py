import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno

from test import support

# A mixin for testing RawIOBase.
class RawIOMixin:

    # Subclasses should override.
    def new_io(self):
        raise NotImplementedError

    def test_read(self):
        io = self.new_io()
        self.assertRaises(TypeError, io.read)
        self.assertRaises(TypeError, io.read, 'x')
        self.assertRaises(TypeError, io.read, None)
        self.assertRaises(TypeError, io.read, 1, 'x')
        self.assertRaises(TypeError, io.read, 1, None)
        self.assertRaises(TypeError, io.read, 1, 2, 3)
        self.assertRaises(TypeError, io.read, 1, 2, None)
        self.assertRaises(ValueError, io.read, -1)
        self.assertRaises(Value
