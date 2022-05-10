import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import weakref
import pickle
import gc
from test import support

# A mixin for testing RawIOBase's readinto() method.
class ReadintoMixin:

    def test_readinto(self):
        b = bytearray(self.mymemoryview(b"hello"))
        n = self.io.readinto(b)
        self.assertEqual(n, 5)
        self.assertEqual(b, b"hello")

    def test_readinto_non_contiguous(self):
        b = bytearray(self.mymemoryview(b"hello"))
        n = self.io.readinto(b[::2])
        self.assertEqual(n, 3)
        self.assertEqual(b, b"hlelo")

    def test_readinto_resize(self):
        b = bytearray(self.mymemoryview(b"hello"))
        n = self.io.readinto(b)
