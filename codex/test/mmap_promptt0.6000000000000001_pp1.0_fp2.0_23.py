import mmap
# Test mmap.mmap functionality.
#
# This is a test for the mmap module. The purpose of this test is to verify
# that mmap.mmap objects can be created and safely used.
#
# This test was originally written to verify a fix for a bug that caused
# segmentation faults when creating mmap.mmap objects on Linux.
#
# Written by: Greg Chapman, gregchap@gmail.com
# Date: February 2009
#
# This code is in the public domain


import unittest
import mmap
import os
import os.path
import sys
import tempfile

import mmap_test_support

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.temp_file_path = tempfile.mktemp()

    def tearDown(self):
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

