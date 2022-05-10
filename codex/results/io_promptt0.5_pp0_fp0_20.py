import io
# Test io.RawIOBase.readinto() and io.RawIOBase.write()

import io
import os
import unittest
from test import support

class RawIOBaseTestCase(unittest.TestCase):
    def setUp(self):
        self.f = io.BytesIO(b"abc\n")

    def test_readinto(self):
        b = bytearray(3)
        n = self.f.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"abc")

    def test_write(self):
        n = self.f.write(b"xy")
        self.assertEqual(n, 2)
        self.assertEqual(self.f.getvalue(), b"xyc\n")

    def test_writelines(self):
        n = self.f.writelines([b"x", b"y"])
        self.assertEqual(n, None)
        self.assertEqual(self.f.getvalue(), b"xyabc\n")

    def
