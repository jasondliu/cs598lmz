import io
# Test io.RawIOBase

import unittest

from test import support
from test.support import _2G, _4G

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Test io.RawIOBase
        self.assertIsInstance(io.RawIOBase(), io.IOBase)
        self.assertIsInstance(io.RawIOBase(), io.RawIOBase)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase)

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
                return len(b)

        rawio = TestRawIO()
        b = bytearray(5)
        n = rawio.readinto(b)
        self.assertEqual(n, 5)
        self.assert
