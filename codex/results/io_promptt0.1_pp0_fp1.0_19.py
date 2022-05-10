import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import errno
import tempfile
import random
import warnings
import contextlib
import pickle
import gc
import shutil

from test import support
from test.support import import_fresh_module

# Base class for testing io.RawIOBase
class BaseRawIOBaseTests(object):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.readinto, bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.write, b'')

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.fileno)

    def test_isatty(self):
        self.assertFalse(self.IO.isatty())

    def test_seek(self
