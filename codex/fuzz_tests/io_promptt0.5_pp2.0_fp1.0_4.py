import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import _io

from test import test_support

# Base class for testing io.RawIOBase.
#
# Implementations should define a setUp method that creates an instance
# self.r of the object to be tested.
#
# The test_xxx() methods should not make any assumptions about the
# concrete implementation (except for the .closed attribute, which
# should be tested).

class BaseRawIOBaseTests:

    def test_read(self):
        b = self.r.read(1)
        self.assertEqual(b, b"x")
        self.assertEqual(self.r.read(0), b"")
        self.assertRaises(TypeError, self.r.read, None)

    def test_readinto(self):
        b = bytearray(b"x")
        n = self.r.readinto(b)
        self.assertEqual(n, 1)
        self.assertEqual(b, b"
