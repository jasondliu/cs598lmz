import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Issue #11459: io.RawIOBase should be a virtual base class.
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        f = io.BytesIO(b"ABCDE")
        self.assertEqual(f.read(0), b"")
        self.assertEqual(f.read(1), b"A")
        self.assertEqual(f.read(2), b"BC")
        self.assertEqual(f.read(3), b"DE")
        self.assertEqual(f.read(4), b"")
        self.assertEqual(f.read(1), b"")
        f.close()

    def test_readinto(self):
        f = io.BytesIO(b"ABCDE")
        b = bytearray(3)
        self.
