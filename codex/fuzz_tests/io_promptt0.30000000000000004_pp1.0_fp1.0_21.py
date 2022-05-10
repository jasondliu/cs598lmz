import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref
import sys
import threading
import time
import os
import errno
import select
import struct
import socket
import tempfile
import warnings

from test import support
from test.support import TESTFN, run_with_locale, import_module, unlink, \
    findfile, cpython_only, check_warnings

# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)
        self.assertRaises(TypeError, io.RawIOBase, None)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_readall(self):
        self.assertRaises(io
