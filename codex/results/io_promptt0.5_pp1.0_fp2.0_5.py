import io
# Test io.RawIOBase

import sys
import unittest
from test import support
from test.support import TESTFN, unlink

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'wb')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_raw_read(self):
        # Test RawIOBase.read()
        self.assertRaises(io.UnsupportedOperation, self.f.read)
        self.f.close()
        self.f = None

        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b"xyz" * n
        r = MyRawIO()
        self.assertEqual(r.read(3), b"xyz")
        self.assertEqual(r.read(2), b"xyzxyz")
        self.assertEqual(r.read(), b"xyzxyzxyz")

