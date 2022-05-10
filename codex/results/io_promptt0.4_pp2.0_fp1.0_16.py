import io
# Test io.RawIOBase.readinto()

import unittest

from test import support
from test.support import TESTFN, run_unittest

class TestRawIO(unittest.TestCase):
    def setUp(self):
        self.f = open(TESTFN, 'wb')

    def tearDown(self):
        self.f.close()
        support.unlink(TESTFN)

    def test_readinto(self):
        self.f.write(b'abcdefgh')
        self.f.close()

        f = open(TESTFN, 'rb')
        b = bytearray(b'xxxxxxx')
        n = f.readinto(b)
        self.assertEqual(n, len(b))
        self.assertEqual(b, bytearray(b'abcdefg'))
        self.assertEqual(f.readinto(b), 0)
        f.close()

    def test_readinto_array(self):
        import array
        self.f.write(b'abcdefgh')
       
