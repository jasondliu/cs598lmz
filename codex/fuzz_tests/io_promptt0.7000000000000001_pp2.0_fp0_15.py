import io
# Test io.RawIOBase.readall() and io.RawIOBase.readinto()
import unittest

from test.support import TESTFN, run_unittest

class TestReadall(unittest.TestCase):
    def setUp(self):
        self.f = io.BytesIO(b"abc")

    def tearDown(self):
        self.f.close()

    def test_readall(self):
        s = self.f.readall()
        self.assertEqual(s, b"abc")
        self.assertEqual(self.f.tell(), 3)

    def test_readinto(self):
        b = bytearray(b"xxxxx")
        n = self.f.readinto(b)
        self.assertEqual(b[:3], b"abcx")
        self.assertEqual(n, 3)

    def test_readinto_no_len(self):
        b = []
        n = self.f.readinto(b)
        self.assertEqual(b, [])
        self.assertE
