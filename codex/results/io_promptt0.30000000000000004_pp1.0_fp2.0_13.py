import io
# Test io.RawIOBase.readinto()

import _io
import io
import sys
import unittest
from test import support

class TestRawIO(unittest.TestCase):

    def test_readinto(self):
        # SF bug #1074366:  io.RawIOBase.readinto() should return
        # the number of bytes read.
        class MyRawIO(_io.RawIOBase):
            def readinto(self, b):
                return 0
        rawio = MyRawIO()
        b = bytearray(10)
        self.assertEqual(rawio.readinto(b), 0)
        self.assertEqual(len(b), 10)

    def test_readinto_negative_arg(self):
        # Issue #17078: readinto() should not accept negative argument
        class MyRawIO(_io.RawIOBase):
            def readinto(self, b):
                return 0
        rawio = MyRawIO()
        b = bytearray(10)
        self.assertRaises(ValueError, rawio.readinto, b
