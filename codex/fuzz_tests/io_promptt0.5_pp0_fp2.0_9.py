import io
# Test io.RawIOBase

import unittest
import io
import os

from test import support

class RawIOTest(unittest.TestCase):

    def test_raw_io_default(self):
        # Test default values
        rawio = io.RawIOBase()
        self.assertEqual(rawio.mode, 'x')
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, rawio.write, b'')
        self.assertRaises(io.UnsupportedOperation, rawio.seek, 0)
        self.assertRaises(io.UnsupportedOperation, rawio.tell)
        self.assertRaises(io.UnsupportedOperation, rawio.truncate)
        self.assertRaises(io.UnsupportedOperation, rawio.fileno)
        self.assertRaises(io.UnsupportedOperation, rawio.isatty)
        self.assertRaises(
