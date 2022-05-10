import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import pickle
import errno
import gc

from test import support

# A mixin for testing RawIOBase objects that are not seekable.
class NonSeekableRawMixin:

    def test_read_non_blocking(self):
        # Issue #11459: calling RawIOBase.read() with a size of 0 should
        # return b'' instead of None.
        self.assertEqual(self.io.read(0), b'')

    def test_readinto_non_blocking(self):
        # Issue #11459: calling RawIOBase.readinto() with a size of 0 should
        # return 0 instead of None.
        self.assertEqual(self.io.readinto(bytearray()), 0)

    def test_read_non_blocking_negative(self):
        # Issue #11459: calling RawIOBase.read() with a negative size should
        # raise ValueError.
        self.assertRaises(ValueError, self.
