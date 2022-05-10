import mmap
# Test mmap.mmap(-1, length, access=mmap.ACCESS_WRITE)
#
# This test is to check that mmap(-1, length, access=mmap.ACCESS_WRITE)
# works.  mmap(-1, length, access=mmap.ACCESS_WRITE) maps the
# anonymous memory region.
#
# This test is not run by default.  To run this test, specify the
# test name (mmap_anonymous) to the mmap test script.
#
# This test is derived from mmap_write_test.py

import os
import mmap
import unittest

from test.support import run_unittest, TESTFN, unlink, check_syntax

class MmapWriteTests(unittest.TestCase):

    def setUp(self):
        self.filename = TESTFN
        f = open(self.filename, 'wb+')
        f.write(b'\0' * mmap.ALLOCATIONGRANULARITY)
        f.close()

