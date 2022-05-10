import mmap
# Test mmap.mmap()
#
# This test is designed to test the mmap module's mmap() function.  It is
# not designed to test the functionality of the mmap object.
#
# The test creates a file of size MMAP_SIZE and writes the string
# "*<MMAP_SIZE>*" to it.  It then mmaps the file and verifies that the
# contents of the mmap are correct.  It then writes the string "*<MMAP_SIZE>*"
# to the mmap and verifies that the file has been updated.

import os
import mmap
import unittest
import tempfile

MMAP_SIZE = 1024

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.filename = tempfile.mktemp()
        f = open(self.filename, 'wb+')
        f.write(b'*' * MMAP_SIZE)
        f.close()

    def tearDown(self):
        os.unlink(self.filename)

