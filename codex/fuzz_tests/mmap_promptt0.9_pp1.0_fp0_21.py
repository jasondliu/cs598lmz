import mmap
# Test mmap.mmap() and mmap.mmap() with the MAP_PRIVATE flag.
# Windows requires write access to the file. (That ought to be
# optional!)
import os
import sys
import tempfile
import unittest

if sys.platform == 'darwin':
    raise unittest.SkipTest("Known to fail on OSX Tiger/PPC")

class MmapTestsWithPriv(unittest.TestCase):
    # Requires write access to the file to be mapped.
    filename = 'mmaptest.dat'
    size = 1024

    def setUp(self):
        self.data = b'\x00' * self.size
        f = open(self.filename, 'wb+')
        f.write(self.data)
        f.close()

    def tearDown(self):
        if os.path.exists(self.filename):
            os.unlink(self.filename)

    def _test_writes(self, py_str, testfunc):
        # set the initial values
        data = bytearray(self.data)

