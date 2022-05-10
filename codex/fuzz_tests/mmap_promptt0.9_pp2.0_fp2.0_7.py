import mmap
# Test mmap.mmap handling.

import random, os.path
from test import support

import mmap
import _testcapi


LOG_PATH = os.path.join(support.TESTFN, "mmap_log")
LOG_SIZE = 8 * mmap.ALLOCATIONGRANULARITY

class BaseMMapTests:
    filename = support.TESTFN
    size = 1024
    access = mmap.ACCESS_READ

    def setUp(self):
        fp = open(self.filename, 'w+b')
        try:
            fp.write(b'\0' * self.size)
        finally:
            fp.close()

    def tearDown(self):
        support.unlink(self.filename)

    def open(self, flags):
        fp = open(self.filename, flags)
        try:
            return mmap.mmap(fp.fileno(), self.size, self.access)
        finally:
            fp.close()

    def read(self, x):
        self.assertEqual(x[0
