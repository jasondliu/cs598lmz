import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import pickle
import gc
import contextlib

from test import support

# Base class for testing a RawIOBase implementation.
class BaseRawTests(object):
    # Subclass must define a read() method.
    def read(self, n=-1):
        raise NotImplementedError

    def test_read(self):
        b = self.read(0)
        self.assertEqual(b, b"")
        b = self.read(1)
        self.assertEqual(b, b"x")
        b = self.read(2)
        self.assertEqual(b, b"yz")
        b = self.read(3)
        self.assertEqual(b, b"")
        b = self.read(4)
        self.assertEqual(b, b"")

    def test_readall(self):
        b = self.readall()
        self.assertEqual(b, b"
