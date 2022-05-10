import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref

from test import support

# A mixin for testing RawIOBase
class BaseRawIOTest:
    # Subclasses must define the following attributes:
    # - self.thetype
    # - self.basetype
    # - self.bytes

    def test_constructor(self):
        b = self.thetype(self.bytes)
        self.assertEqual(b.read(), self.bytes)
        self.assertEqual(b.read(), b"")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(-1), b"")
        self.assertEqual(b.readinto(bytearray()), 0)
        self.assertEqual(b.readinto(bytearray(0)), 0)
        self.assertEqual(b.readinto(bytearray(-1)), 0)
        self.assertEqual(b.readinto(bytearray(1
