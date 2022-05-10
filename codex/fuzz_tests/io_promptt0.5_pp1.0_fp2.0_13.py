import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Simple test to check RawIOBase
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, f.readline)
        self.assertRaises(io.UnsupportedOperation, f.write, b"")
        self.assertRaises(io.UnsupportedOperation, f.seek, 0)
        self.assertRaises(io.UnsupportedOperation, f.tell)
        self.assertRaises(io.UnsupportedOperation, f.truncate, 0)
        self.assertEqual(f.readable(), False)
        self.assertEqual(f.writable(), False)
        self.assertEqual(f.seekable(), False)
        self.assertEqual(f.isatty
