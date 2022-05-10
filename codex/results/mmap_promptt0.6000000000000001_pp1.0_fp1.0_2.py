import mmap
# Test mmap.mmap.
import os
# Test os.open, os.close, os.write, os.read.
import time
# Test time.sleep.

import ctypes
# Test ctypes.memmove.

from mmap import _mmap

from test.support import run_unittest, import_module, unlink, TESTFN, findfile

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.f = open(TESTFN, "w+b")
        self.f.write(b"\0" * mmap.PAGESIZE)
        self.f.flush()

    def tearDown(self):
        self.f.close()
        unlink(TESTFN)


    def test_bad_args(self):
        # Try a bunch of invalid calls to mmap.mmap.
        self.assertRaises(ValueError, mmap.mmap, -1, 1)
        self.assertRaises(ValueError, mmap.mmap, -1, 1, mmap.MAP_SHARED
