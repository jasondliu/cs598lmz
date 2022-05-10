import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOBaseTestCase(unittest.TestCase):

    def test_readinto(self):
        # Test readinto()
        b = bytearray(b"abc")
        f = io.BytesIO(b)
        n = f.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"abc")
        n = f.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(b, b"abc")
        f.close()

        b = bytearray(b"abc")
        f = io.BytesIO(b)
        n = f.readinto(memoryview(b))
        self.assertEqual(n, 3)
        self.assertEqual(b, b"abc")
        n = f.readinto(memoryview(b))
        self.assertEqual(n, 0)
        self.assertEqual(b, b"abc")
        f
