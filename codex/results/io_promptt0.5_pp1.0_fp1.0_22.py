import io
# Test io.RawIOBase.

import io
import os
import sys
import unittest
from test import support

# A mixin for testing IOBase
class BaseTestIOBase:

    def test_attributes(self):
        self.assertEqual(self.IOBase.closed, False)
        self.assertEqual(self.IOBase.mode, '')
        self.assertEqual(self.IOBase.name, '')
        self.assertEqual(self.IOBase.newlines, None)
        self.assertEqual(self.IOBase.encoding, None)
        self.assertEqual(self.IOBase.errors, None)
        self.assertEqual(self.IOBase.line_buffering, False)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.IOBase.read)
        self.assertRaises(io.UnsupportedOperation, self.IOBase.read, 10)

    def test_readinto(self):
        b = bytearray(self.sample_size)
        n =
