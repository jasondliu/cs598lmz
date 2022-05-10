import mmap
# Test mmap.mmap.move

import os, tempfile, mmap, unittest
from test import test_support

class MmapTestCase(unittest.TestCase):
    def setUp(self):
        fd, self.filename = tempfile.mkstemp()
        os.close(fd)

    def tearDown(self):
        os.unlink(self.filename)

    def test_move(self):
        # Create a file of size one page.
        f = open(self.filename, 'wb')
        try:
            f.write('\0' * mmap.PAGESIZE)
        finally:
            f.close()

        # mmap the file.
        f = open(self.filename, 'r+b')
