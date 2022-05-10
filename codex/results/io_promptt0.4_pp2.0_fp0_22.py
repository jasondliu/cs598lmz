import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import errno
import tempfile
import functools

from test import support
from test.support import _2G, _4G

# A mixin class to provide a default implementation of
# test_readinto_small_buffer.
class SmallBuffersMixin:
    def test_readinto_small_buffer(self):
        # Issue #7995: readinto() with a small buffer
        self.assertEqual(self.io.readinto(bytearray(1)), 1)
        self.assertEqual(self.io.readinto(bytearray(1)), 1)
        self.assertEqual(self.io.readinto(bytearray(1)), 1)
        self.assertEqual(self.io.readinto(bytearray(1)), 0)

class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.io.read
