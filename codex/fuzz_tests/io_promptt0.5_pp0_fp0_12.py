import io
# Test io.RawIOBase

import _io
import unittest
from test import support

try:
    import threading
except ImportError:
    threading = None

try:
    import os
    DEVNULL = os.devnull
except (AttributeError, ImportError):
    DEVNULL = "/dev/null"


class RawIOTest(unittest.TestCase):

    def test_abc(self):
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase))
        self.assertIsInstance(io.RawIOBase(), io.IOBase)
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write)

    def test_
