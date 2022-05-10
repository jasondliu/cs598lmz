import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support

# A mixin for testing RawIOBase objects that are stream-like.
# Stream-like RawIOBase objects are those that have readinto,
# readinto1, and read1 methods.
class StreamLikeRawIOMixin:

    # A mixin for testing RawIOBase objects that are stream-like.
    # Stream-like RawIOBase objects are those that have readinto,
    # readinto1, and read1 methods.
    def test_readinto(self):
        # Read into a buffer
        b = bytearray(self.size)
        n = self.io.readinto(b)
        self.assertEqual(n, self.size)
        self.assertEqual(b, self.get_sample_data())

    def test_readinto_small_buffer(self):
        # Read into a small buffer
        b = bytearray(1)
        n = self.io.readinto(b)
        self.assertEqual(
