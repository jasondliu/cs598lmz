import mmap
# Test mmap.mmap(0, 1)
# This is a test case for SF bug #1534662.
import os
import stat
import sys
import tempfile
import unittest
from test import support
from test.support import TESTFN, unlink, run_unittest

class MmapTests(unittest.TestCase):
    @unittest.skipUnless(hasattr(os, "fork"), "requires os.fork()")
    def test_flush_after_fork(self):
        # Issue #15301: flush() shouldn't raise an error after fork()
        fd = os.open(TESTFN, os.O_CREAT | os.O_RDWR)
        os.write(fd, b"ABC")
        os.lseek(fd, 0, 0)
        m = mmap.mmap(fd, 3)
        m.read(1)
        pid = os.fork()
        if pid == 0:
            # child
            self.assertEqual(m.flush(), None)
            os._exit(0)
