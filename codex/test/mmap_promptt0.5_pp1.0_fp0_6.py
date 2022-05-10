import mmap
# Test mmap.mmap
import os
import sys
import unittest
import warnings
import weakref

from test import support

TESTFN = support.TESTFN

# This is the default size used by the Unix implementation of mmap.  We use
# the same size here so that we can rely on the underlying mmap module having
# a specific allocation granularity.
ALLOCATIONGRANULARITY = mmap.ALLOCATIONGRANULARITY

PAGESIZE = mmap.PAGESIZE

# Windows has different error codes, so we can't use assertRaises()
# to check for them.
class MmapTests(unittest.TestCase):
    def setUp(self):
        self.f = open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        if os.path.exists(TESTFN):
            os.unlink(TESTFN)

