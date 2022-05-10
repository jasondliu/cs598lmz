import io
# Test io.RawIOBase

import os
import sys
import unittest
from test import support
try:
    import threading
except ImportError:
    threading = None

# Base class for testing io.RawIOBase
class RawIOTest:
    # Subclass must override
    def new_instance(self):
        raise NotImplementedError

    def test_read(self):
        rawio = self.new_instance()
        self.assertEqual(rawio.read(0), b'')
        self.assertRaises(TypeError, rawio.read, None)
        self.assertRaises(ValueError, rawio.read, -1)

    def test_readinto(self):
        rawio = self.new_instance()
        b = bytearray(5)
        n = rawio.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(len(b), 5)
        self.assertRaises(TypeError, rawio.readinto, memoryview(b))
        self.assertRaises(Type
