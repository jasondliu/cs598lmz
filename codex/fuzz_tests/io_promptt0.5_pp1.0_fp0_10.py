import io
# Test io.RawIOBase.readinto()

import io
import os
import sys
import unittest
import weakref

from test import support

# Issue #10935: io.RawIOBase.readinto() should raise a ValueError
# if the object has been closed.
class TestReadInto(unittest.TestCase):

    def test_readinto_after_close(self):
        f = io.BytesIO(b"abc")
        f.close()
        self.assertRaises(ValueError, f.readinto, bytearray(1))

# Issue #14406: io.RawIOBase.readinto() should accept any kind of buffer
# object.
class TestReadIntoBuffer(unittest.TestCase):

    def test_readinto_memoryview(self):
        f = io.BytesIO(b"abc")
        b = memoryview(bytearray(1))
        n = f.readinto(b)
        self.assertEqual(n, 1)
        self.assertEqual(b[:], b"a")

    def test
