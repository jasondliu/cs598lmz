import mmap
# Test mmap.mmap_buffer
#
# $Id$
#
#  Copyright (C) 2005-2012   Gregory P. Smith (greg@krypto.org)
#  Licensed to PSF under a Contributor Agreement.

import unittest
import sys
import mmap
from mmap import mmap_buffer
import gc
import _testcapi

class MmapBufferTestCase(unittest.TestCase):

    filename = sys.executable

    def test(self):
        # Test the mmap_buffer() function.
        f = open(self.filename, 'r')
        try:
            m1 = mmap_buffer(f, mmap.MAP_PRIVATE)
            m2 = mmap_buffer(f, mmap.MAP_PRIVATE)
        finally:
            f.close()
        self.assertEqual(m1[:], m2[32:])
        # Verify m1 and m2 are different objects.
        self.assertNotEqual(id(m1), id(m2))
        # Verify the objects are instances of mmap_
