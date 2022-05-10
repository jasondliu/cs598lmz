import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap documentation.
#
# This test is not run by default.  To run it, do:
#
#   python test_mmap.py

import os
import unittest
import mmap

from test import test_support

# The filename used for testing
if os.name == 'nt':
    filename = r'c:\temp\mmaptest.dat'
else:
    filename = '/tmp/mmaptest.dat'

# The size of the file used for testing
filesize = 1024

class MmapTests(unittest.TestCase):
    def setUp(self):
        # Create a file to be mmap'ed.
        f = open(filename, 'w+b')
        try:
            # zero-fill the file
            f.seek(filesize-1)
            f.write('\x00')
        finally:
            f.close()

    def tearDown(self):
        os.unlink(filename)

