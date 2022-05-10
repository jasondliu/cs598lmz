import io
# Test io.RawIOBase.readinto

import _io
import io
import unittest

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        b = bytearray(b"abc")
        f = io.BytesIO(b)
        n = f.readinto(memoryview(b))
        self.assertEqual(n, 3)
        self.assertEqual(b, b"abc")

        n = f.readinto(memoryview(b))
        self.assertEqual(n, 0)

        f = io.BytesIO(b"abc")
        n = f.readinto(memoryview(b), 1)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"aabc")

        n = f.readinto(memoryview(b), 1)
        self.assertEqual(n, 0)

        f = io.BytesIO(b"abc")
        n = f.readinto(memoryview(b), 1, 1)
