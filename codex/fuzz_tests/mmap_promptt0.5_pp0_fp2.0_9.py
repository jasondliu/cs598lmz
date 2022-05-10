import mmap
# Test mmap.mmap()
#
# This test tries to mmap a file that doesn't exist.
#
# MMAP_FILE is a file that will be created by this test.
#
# This test is supposed to fail.
#
# This test was written by Andrew Johnson <ajohnson@redhat.com>
#

import os
import sys
import unittest
import test.support
import mmap

MMAP_FILE = test.support.TESTFN

class MmapTestCase(unittest.TestCase):

    def test_mmap(self):
        try:
            fd = os.open(MMAP_FILE, os.O_RDWR | os.O_CREAT)
            os.close(fd)
            f = open(MMAP_FILE, "r+b")
            size = 1024
            m = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_WRITE)
            self.assertEqual(len(m), size)
            self.assertEqual(m[0:5], b'\0\0\
