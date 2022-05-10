import mmap
# Test mmap.mmap.read() and mmap.mmap.write()

# mmap.mmap.read() and mmap.mmap.write() are not supported on Windows
# before 3.2.
# https://bugs.python.org/issue14403

import os
import unittest
from test import support
from test.support import import_module
from test.support import TESTFN, unlink

try:
    mmap = import_module('mmap')
except ImportError:
    raise unittest.SkipTest("requires mmap module")

class MmapReadTestCase(unittest.TestCase):
    def setUp(self):
        unlink(TESTFN)
        with open(TESTFN, "wb") as f:
            f.write(b"0123456789")

    def tearDown(self):
        unlink(TESTFN)

    def test_read_0(self):
        with open(TESTFN, "rb") as f:
            m = mmap.mmap(f.fileno(), 10, access=mmap.ACC
