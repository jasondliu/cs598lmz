import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import _pyio as pyio

from test import support
from test.support import import_fresh_module

# Base class for testing a RawIO implementation.
# Subclasses must override read(), readall() and seek(),
# and set the readable and writable attributes.
class BaseTestRawIO(object):
    # Subclass must override
    def read(self, n=-1):
        raise NotImplementedError

    # Subclass must override
    def readall(self):
        raise NotImplementedError

    # Subclass must override
    def seek(self, n, whence=0):
        raise NotImplementedError

    # Subclass must override
    def readable(self):
        raise NotImplementedError

    # Subclass must override
    def writable(self):
        raise NotImplementedError

    def test_read(self):
        self.assertEqual(self.read(), b'\x00')
        self.assertEqual(
