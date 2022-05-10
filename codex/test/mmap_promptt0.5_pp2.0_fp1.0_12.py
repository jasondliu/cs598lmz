import mmap
# Test mmap.mmap() and mmap.MAP_PRIVATE.
#
# This test is a little odd, since it uses an anonymous mmap() as a scratch
# space to test the mmap module.  The reason for this is that it's too
# difficult to write a file that's known to be exactly the right size.

import mmap
import os
import stat
import sys
import unittest

class MmapTests(unittest.TestCase):

    def test_anonymous(self):
        # Try it with an anonymous mmap.
        m = mmap.mmap(-1, 1024)
        m.write(b"abcde")
        m.flush()
        m.seek(0)
        self.assertEqual(m.read(5), b"abcde")
        m.close()

    def test_filename(self):
        # Try it with a named file.
        filename = "mmap_test"
        fd = os.open(filename, os.O_CREAT | os.O_RDWR)
