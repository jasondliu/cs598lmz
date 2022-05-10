import mmap
# Test mmap.mmap behaviour when offset + size > length of file
# and when (offset + size) wraps in 32-bit space.

import mmap
import os
import sys
import unittest


class MmapTooBigTest(unittest.TestCase):
    def test_read(self):
        # Open file of specified size
        size = 0x10000000  # ~256MB
        f = open(TESTFN2, 'wb+')
        f.seek(size-1)
        f.write(b'\0')
        f.flush()
        f.seek(0)

        # Now try to map a region past the end of the file
        m = mmap.mmap(f.fileno(), size+1, access=mmap.ACCESS_READ)
        self.assertEqual(len(m), size)

        # Unmap to make sure nothing is broken
        m.close()

    def test_write(self):
        # Open file of specified size
        size = 0x10000000  # ~256MB
        f = open(TESTFN2, 'wb
