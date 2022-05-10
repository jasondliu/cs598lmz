import mmap
# Test mmap.mmap.readline()
#
# This test checks that mmap.mmap.readline() works correctly, even
# when the file size is not a multiple of the page size.
#
# The test creates a file, maps it, and then checks that the first
# line of the file is read correctly.
#
# The test passes if the line read from the mmap'd file is the same
# as the line written to the file.
#
# The test fails if the line read from the mmap'd file is not the
# same as the line written to the file.

try:
    from test import support
except ImportError:
    from test import test_support as support

import os
import unittest

class MmapTests(unittest.TestCase):
    def setUp(self):
        # Create a file
        fd = os.open(support.TESTFN, os.O_RDWR | os.O_CREAT)

        # Write a line to the file
        os.write(fd, b"hello world\n")

        # Map the file, with copy
