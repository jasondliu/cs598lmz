import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import bigmemtest

# Issue #7995: io.RawIOBase.readinto() should not accept negative arguments
class TestRawIOBaseNegativeReadinto(unittest.TestCase):
    def test_negative_readinto(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return super().readinto(b)

        rawio = MyRawIO()
        self.assertRaises(ValueError, rawio.readinto, bytearray(-1))

# Issue #7995: io.RawIOBase.readinto() should not accept negative arguments
class TestRawIOBaseNegativeReadinto(unittest.TestCase):
    def test_negative_readinto(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return super().readinto(b)

        rawio = MyRawIO()
        self.assertRaises(ValueError, rawio.readinto, bytearray(-1
