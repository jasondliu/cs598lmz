import io
# Test io.RawIOBase.readinto()

from io import BytesIO
from test.support import import_module
import unittest

# io is an optional module, so SkipTest if it's not available
io = import_module('io')

class TestRawIO(unittest.TestCase):
    def setUp(self):
        self.r = io.RawIOBase()
        self.r.__init__(b"abc")

    def test_readinto(self):
        b = bytearray(2)
        n = self.r.readinto(b)
        self.assertEqual(n, 2)
        self.assertEqual(b, b"ab")

    def test_readinto_array(self):
        import array
        b = array.array('b', range(4))
        n = self.r.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b[:3], array.array('b', b'abc'))

    def test_readinto_readall(self):
        b
