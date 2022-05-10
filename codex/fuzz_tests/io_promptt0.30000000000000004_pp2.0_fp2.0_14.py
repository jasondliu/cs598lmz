import io
# Test io.RawIOBase.readinto()

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Issue #11458: io.RawIOBase.readinto() should not accept negative arguments
class TestReadintoNegative(unittest.TestCase):
    def setUp(self):
        self.f = io.BytesIO(b"abc")

    def test_readinto_negative(self):
        b = bytearray(1)
        self.assertRaises(ValueError, self.f.readinto, b, -1)
        self.assertRaises(ValueError, self.f.readinto, b, -1, -1)
        self.assertRaises(ValueError, self.f.readinto, b, -1, 1)
        self.assertRaises(ValueError, self.f.readinto, b, 1, -1)

    def test_readinto_negative_bytearray(self):
        b = bytearray(1)
        self.assertRaises
