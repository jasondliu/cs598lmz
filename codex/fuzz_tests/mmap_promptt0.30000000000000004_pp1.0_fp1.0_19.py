import mmap
# Test mmap.mmap()
#
# This test is a little different from the other mmap tests.  It
# doesn't use the mmap module at all.  Instead, it uses the os.open()
# and os.write() calls to put data into a file, and then uses the
# mmap.mmap() call to map that data into memory.
#
# The reason for this is that the mmap module has a bug on Windows
# that causes it to fail when the file is opened with os.O_CREAT.  The
# workaround is to open the file without os.O_CREAT, write data to it,
# and then use mmap to map it.

import os
import sys
import unittest
from test import support
import mmap

FILENAME = support.TESTFN

class MmapTests(unittest.TestCase):
    def setUp(self):
        # Create a file to be mmap'ed.
        f = open(FILENAME, 'wb+')
        try:
            # We'll map a few different-sized views of the file
            f.
