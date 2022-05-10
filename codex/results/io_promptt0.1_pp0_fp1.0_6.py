import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Issue #7995: io.RawIOBase.readinto() should return None
# when the argument is 0-length.

class TestRawIOBase(unittest.TestCase):
    def test_readinto_zero_length(self):
        f = io.BytesIO(b'abc')
        self.assertEqual(f.readinto(bytearray()), None)
        self.assertEqual(f.readinto(bytearray(0)), None)
        self.assertEqual(f.readinto(memoryview(bytearray(0))), None)

    def test_readinto_non_zero_length(self):
        f = io.BytesIO(b'abc')
        b = bytearray(1)
        self.assertEqual(f.readinto(b), 1)
        self.assertEqual(b, b'a')
        self.assertEqual(f
