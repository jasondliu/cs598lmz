import io
# Test io.RawIOBase.readinto

import io
import _pyio as pyio
import sys
import unittest
from test import support
from test.support import bigmemtest

try:
    from io import BlockingIOError
except ImportError:
    BlockingIOError = None

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        b = bytearray(10)
        n = io.BytesIO(b'1234567890').readinto(b)
        self.assertEqual(n, len(b))
        self.assertEqual(b, b'1234567890')
        self.assertRaises(TypeError, io.BytesIO().readinto, memoryview(b'123'))

    def test_readinto_negative_size(self):
        b = bytearray(10)
        with self.assertRaises(ValueError):
            io.BytesIO(b'1234567890').readinto(b, -1)

    def test_readinto_negative_offset(self):
        b =
