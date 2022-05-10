import mmap
# Test mmap.mmap()
#
# This test checks that mmap.mmap() works with a file descriptor.
#
# This test is based on test_mmap.py, but uses a file descriptor instead of
# a file name.

import os
import unittest
import mmap
import tempfile
import stat
import sys

from test import support

# Skip this test if the system does not support anonymous mmaps.
try:
    mmap.mmap(-1, 1)
except EnvironmentError:
    raise unittest.SkipTest("system does not support anonymous mmaps")

# Skip this test if the system does not support file descriptors.
try:
    os.open(os.devnull, os.O_RDONLY)
except (AttributeError, OSError):
    raise unittest.SkipTest("system does not support file descriptors")


class MmapTests(unittest.TestCase):
    def setUp(self):
        self.file = tempfile.TemporaryFile()
        self.addCleanup(self.file.close)

