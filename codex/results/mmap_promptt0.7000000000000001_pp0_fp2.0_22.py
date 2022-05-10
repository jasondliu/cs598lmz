import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0)

import os, stat, tempfile, unittest, mmap, re
from test import test_support

try:
    from fcntl import F_GETFL, F_SETFL, O_NONBLOCK
except ImportError:
    O_NONBLOCK = -1
    F_GETFL = -1
    F_SETFL = -1


class MmapTests(unittest.TestCase):
    filename = tempfile.mktemp()
    size = 1024

    def setUp(self):
        fp = open(self.filename, 'wb+')
        self.addCleanup(fp.close)
        fp.write(b'\0' * self.size)
        fp.seek(0)
        self._mmap = mmap.mmap(fp.fileno(), self.size)

    def tearDown(self):
        self._mmap.close()
        os.unlink(self.filename)

    def test_move(self):
