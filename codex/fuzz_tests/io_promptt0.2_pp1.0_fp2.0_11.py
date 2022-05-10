import io
# Test io.RawIOBase

import io
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Read method
        f = io.BytesIO(b"ABCDE")
        self.assertEqual(f.read(0), b"")
        self.assertEqual(f.read(1), b"A")
        self.assertEqual(f.read(2), b"BC")
        self.assertEqual(f.read(3), b"DE")
        self.assertEqual(f.read(4), b"")
        self.assertEqual(f.read(1), b"")

    def test_readall(self):
        # Readall method
        f = io.BytesIO(b"ABCDE")
        self.assertEqual(f.readall(), b"ABCDE")
        self.assertEqual(f.readall(), b"")

    def test_readinto(self):
       
