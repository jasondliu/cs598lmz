import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
import weakref
from test import support
from test.support import TESTFN, unlink

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        f = io.BytesIO(b"abc")
        self.assertEqual(f.read(0), b"")
        self.assertEqual(f.read(1), b"a")
        self.assertEqual(f.read(2), b"bc")
        self.assertEqual(f.read(4), b"")
        self.assertEqual(f.read(), b"")
        self.assertEqual(f.read(), b"")
        f.close()

    def test_readall(self):
        # Test RawIOBase.readall()
        f = io.BytesIO(b"abc")
        self.assertEqual(f.readall(), b"abc")
        self.assertEqual(f.readall(), b"")
