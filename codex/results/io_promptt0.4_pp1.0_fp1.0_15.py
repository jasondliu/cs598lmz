import io
# Test io.RawIOBase.readinto()

import _io
import unittest
from test import support

class TestRawIO(unittest.TestCase):

    def test_readinto(self):
        b = bytearray(b'abc')
        f = io.BytesIO()
        n = f.write(b)
        self.assertEqual(n, len(b))
        f.seek(0)
        a = bytearray(3)
        n = f.readinto(a)
        self.assertEqual(n, len(b))
        self.assertEqual(a, b)
        a = bytearray(2)
        n = f.readinto(a)
        self.assertEqual(n, 0)
        self.assertEqual(a, b'\x00\x00')
        self.assertEqual(f.readinto(a), 0)
        f.close()
        self.assertRaises(ValueError, f.readinto, a)

    def test_readinto_array(self):
        b =
