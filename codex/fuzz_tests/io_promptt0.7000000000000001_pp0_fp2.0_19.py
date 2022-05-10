import io
# Test io.RawIOBase

import io
import unittest
from test import support
from test.support.script_helper import assert_python_ok

from io import BytesIO

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Read method
        b = BytesIO(b"abc")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"a")
        self.assertEqual(b.read(2), b"bc")
        self.assertEqual(b.read(4), b"")
        self.assertEqual(b.read(1), b"")
        # Abstract method
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().read)
        self.assertRaises(TypeError, io.RawIOBase().read, "")

    def test_readinto(self):
        # Readinto method
        b = BytesIO(b"abc")
        buf = bytearray(2
