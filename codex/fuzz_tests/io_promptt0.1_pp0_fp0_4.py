import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno

from test import support
from test.support import TESTFN, unlink

# Base class for testing a RawIOBase implementation.
# Subclasses must define a read() method.
class BaseRawIOTest:

    def test_read(self):
        b = self.read(0)
        self.assertEqual(b, b"")
        b = self.read(1)
        self.assertEqual(b, b"a")
        b = self.read(5)
        self.assertEqual(b, b"bcdef")
        b = self.read(1)
        self.assertEqual(b, b"g")
        b = self.read(0)
        self.assertEqual(b, b"")
        b = self.read(1)
        self.assertEqual(b, b"")

    def test_readinto(self):
        b = bytearray(b" " * 10)
        n
