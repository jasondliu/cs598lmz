import mmap
# Test mmap.mmap
#
# This test is not complete, but it does test the basic functionality.
#
# Written by: Andrew Dalke <dalke@dalkescientific.com>
#
# $Id: mmap_test.py,v 1.1 2002/06/06 20:23:08 dalke Exp $
#
# $Log: mmap_test.py,v $
# Revision 1.1  2002/06/06 20:23:08  dalke
# Added tests for mmap.mmap
#
#

import os
import unittest

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.f = open("mmap_test.dat", "wb+")
        self.f.write("\0" * 100)
        self.f.close()
        self.f = open("mmap_test.dat", "rb+")

    def tearDown(self):
        self.f.close()
        os.unlink("mmap_test.dat")

    def test_read(self):
