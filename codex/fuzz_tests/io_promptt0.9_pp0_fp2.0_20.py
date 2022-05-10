import io
# Test io.RawIOBase()

import unittest
from test import support
try:
    import threading
except:
    threading = None


class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        r = io.RawIOBase()
        self.assertFalse(r.seekable())
        self.assertTrue(r.readable())
        self.assertFalse(r.writable())
        self.assertIsNone(r.fileno())
        self.assertRaises(io.UnsupportedOperation, r.isatty)
        self.assertRaises(io.UnsupportedOperation, r.read)
        self.assertRaises(io.UnsupportedOperation, r.readinto, b"")
        self.assertRaises(io.UnsupportedOperation, r.write, b"")
        self.assertRaises(io.UnsupportedOperation, r.tell)
        self.assertRaises(io.UnsupportedOperation, r.seek, 0)
        self.assertRaises(io.UnsupportedOperation, r.truncate)
        self.
