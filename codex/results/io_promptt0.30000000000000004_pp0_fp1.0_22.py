import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import stat
import array
import _pyio as pyio
import weakref
import warnings
import contextlib

from test import support
from test.support import import_fresh_module

# Base class for testing a raw I/O implementation.

class BaseRawIOIntTests(object):

    # Subclass must define a read() method.

    def readinto(self, b):
        data = self.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array) or err.args[0] != "expected read-write buffer, array.array found":
                raise
            b[:n] = array.array('b', data)
        return n

    def test_read(self):
        b = self.read(100)
        self.assertEqual(len(b), 100)

    def test_readall(
