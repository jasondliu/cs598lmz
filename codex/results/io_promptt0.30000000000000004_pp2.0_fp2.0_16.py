import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings
import errno

from test import support
from test.support import import_module

# Skip tests if there is no os.device() method.
device_method = getattr(os, 'device', None)

class RawIOTest:

    # Subclass must override
    def setUp(self):
        self.f = self.factory()
        self.f.__enter__()

    def tearDown(self):
        self.f.__exit__(None, None, None)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.f.write, b'')

    def test_seek(self):
        self.assertRa
