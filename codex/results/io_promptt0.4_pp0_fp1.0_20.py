import io
# Test io.RawIOBase

import sys
import unittest
import weakref

from test import support
from test.support import TESTFN, run_unittest, import_module

# Skip tests if there is no os.sendfile()
try:
    import os
    os.sendfile
except (AttributeError, ImportError):
    raise unittest.SkipTest("os.sendfile() not available")

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = io.BytesIO()
        self.r = io.RawIOBase(self.f)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.r.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.r.readinto, b"")

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.r.write, b"")

    def test_fileno(self):
        self.assertRaises(io
