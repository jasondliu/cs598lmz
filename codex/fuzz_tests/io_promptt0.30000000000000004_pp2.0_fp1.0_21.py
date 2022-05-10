import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import _2G, _4G, _4Gplus1

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Read test
        f = io.BytesIO(b"ABCDE")
        self.assertEqual(f.read(0), b"")
        self.assertEqual(f.read(2), b"AB")
        self.assertEqual(f.read(4), b"CDE")
        self.assertEqual(f.read(1), b"")
        self.assertEqual(f.read(), b"")
        self.assertEqual(f.read(1), b"")
        f.close()

    def test_readline(self):
        # Readline test
        f = io.BytesIO(b"ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXYZ")
        self.assertEqual(f.readline
