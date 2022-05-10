import mmap
# Test mmap.mmap
#
# This is a test of mmap.mmap, not of the mmap module.
#
# This test is not exhaustive.  I have tested only what I have needed.
#
# If you find a bug, have a suggestion, or want to contribute, please email
# me.  My email address may be found on my website at www.aaronsw.com.
#
# Aaron Swartz
# me@aaronsw.com
#
# This code is public domain.

import mmap
import os
import sys
import unittest
import warnings

from test import test_support

# We need to use a real file, because StringIO doesn't seek() properly.
filename = test_support.TESTFN

def write(str):
    f = open(filename, 'wb')
    f.write(str)
    f.close()

class MmapTests(unittest.TestCase):
    def setUp(self):
        write('\x00' * 1024)
