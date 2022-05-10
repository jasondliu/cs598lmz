import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):
    def test_attributes(self):
        self.assertEqual(io.RawIOBase.readable, False)
        self.assertEqual(io.RawIOBase.writable, False)
        self.assertEqual(io.RawIOBase.seekable, False)

    def test_unsupported(self):
        raw = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, raw.read)
        self.assertRaises(io.UnsupportedOperation, raw.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, raw.write, b"")
        self.assertRaises(io.UnsupportedOperation, raw.fileno)
        self.assertRaises(io.UnsupportedOperation, raw.seek, 0)
        self.assertRaises(io.UnsupportedOperation, raw.tell)
        self.assertRaises(io.UnsupportedOperation, raw.truncate)
        self
