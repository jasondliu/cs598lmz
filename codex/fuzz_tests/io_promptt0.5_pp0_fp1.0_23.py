import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support

# A mixin for testing raw I/O
class RawIOMixin:
    def test_read(self):
        self.assertRaises(TypeError, self.io.read)
        self.assertRaises(TypeError, self.io.read, 'x')
        self.assertRaises(TypeError, self.io.read, 1, 'x')
        self.assertRaises(TypeError, self.io.read, 1, 2, 'x')
        self.assertRaises(ValueError, self.io.read, -1)
        self.assertRaises(ValueError, self.io.read, -1, 10)
        self.assertRaises(ValueError, self.io.read, -1, 10, 20)

    def test_readinto(self):
        self.assertRaises(TypeError, self.io.readinto)
        self.assertRaises(TypeError, self.io.readinto, 'x')
        self.assertRaises(
