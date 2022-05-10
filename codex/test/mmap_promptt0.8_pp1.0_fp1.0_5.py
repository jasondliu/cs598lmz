import mmap
# Test mmap.mmap() by comparing the results to the equivalent operations
# performed directly on file objects.
#
# This test assumes that enough memory is available to map at least one copy of
# the entire mapped file.
#
# No effort is made to exercise mmap options, or the msync() method.

import mmap
import os
import tempfile
import unittest
from test import test_support

# A pair of file names; the second one doesn't exist initially.
FILES = [os.path.join(tempfile.gettempdir(), "mmap_file_%d") % i for i in (1, 2)]

# The size of the files we create.
FILE_SIZE = 1024


class MmapTests(unittest.TestCase):
    def setUp(self):
        for file in FILES:
            if os.path.exists(file):
                os.unlink(file)

    def tearDown(self):
        for file in FILES:
            if os.path.exists(file):
                os.unlink(file)

