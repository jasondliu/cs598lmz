import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Issue #11459: io.RawIOBase should have a readable() and writable()
        # method.
        raw = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, raw.readable)
        self.assertRaises(io.UnsupportedOperation, raw.writable)

    def test_io_after_close(self):
        # Issue #11459: calling RawIOBase methods after the raw stream has been
        # closed should raise a ValueError.
        raw = io.RawIOBase()
        raw.close()
        self.assertRaises(ValueError, raw.read, 0)
        self.assertRaises(ValueError, raw.readinto, bytearray())
        self.assertRaises(ValueError, raw.readinto, memoryview(bytearray()))
        self.assertRaises(ValueError, raw.write,
