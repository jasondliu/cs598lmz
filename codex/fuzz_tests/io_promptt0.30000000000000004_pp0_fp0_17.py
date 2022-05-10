import io
# Test io.RawIOBase

import io
import os
import tempfile
import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Issue #17482: io.RawIOBase doesn't have a usable implementation
        # of readinto()
        class MyRawIO(io.RawIOBase):
            def readinto(self, buf):
                return 0
        self.assertEqual(MyRawIO().readinto(bytearray(b'x')), 0)
        self.assertRaises(TypeError, MyRawIO().readinto, memoryview(b'x'))

    def test_readinto_error(self):
        # Issue #17482: io.RawIOBase doesn't have a usable implementation
        # of readinto()
        class MyRawIO(io.RawIOBase):
            def readinto(self, buf):
                raise OSError
        self.assertRaises(OSError, MyRawIO().readinto, bytearray(b'x'))
        self.assertRaises
