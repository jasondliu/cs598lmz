import mmap
# Test mmap.mmap()
#
# This test is a simple example of using mmap.mmap().  It is not
# intended to be a complete test of mmap.mmap().

import mmap
import os
import unittest

from test import test_support

class MmapTests(unittest.TestCase):
    def setUp(self):
        # Create a file to be mmap'ed.
        f = open(test_support.TESTFN, 'w+')
        try:
            # Write 2 zero-byte records.
            f.write('\x00\x00')
            f.write('\x00\x00')
            f.flush()
            self.f = f
        except:
            f.close()
            os.unlink(test_support.TESTFN)
            raise

    def tearDown(self):
        self.f.close()
        os.unlink(test_support.TESTFN)

    def test_basic(self):
        # Open the file, create an mmap'ed region for the whole file,
       
