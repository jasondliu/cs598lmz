import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support

# A mixin class to provide some utility methods for testing RawIOBase
# implementations.

class RawIOMixin:

    def test_read(self):
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(), self.data)
        self.assertEqual(self.io.read(), b'')
        self.assertEqual(self.io.read(), b'')
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(1), b'')
        self.assertEqual(self.io.read(2), b'')
        self.assertEqual(self.io.read(len(self.data)), b'')
        self.assertEqual(self.io.read(len(self.data)+1), b'')

    def test_readinto(self):
        b = bytearray(len
