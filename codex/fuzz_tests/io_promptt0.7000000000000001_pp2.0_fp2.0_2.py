import io
# Test io.RawIOBase

import io
import unittest
import os
import errno

from test import support

# Base class for testing io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.io.read(1)

    def test_readall(self):
        # Test that RawIOBase.readall() returns an empty bytes instance for
        # zero-sized files
        self.assertEqual(self.io.readall(), b'')

    def test_readinto_nonwritable_array(self):
        a = bytearray(5)
        buf = memoryview(a)
        self.assertRaises(BufferError, self.io.readinto, buf)

        # Issue #18757: shouldn't crash
        a = bytearray(5)
        buf = memoryview(a).cast('b')
        self.assertRaises(BufferError, self.io.readinto, buf)

        # Issue #33175: shouldn
