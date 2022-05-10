import mmap
# Test mmap.mmap class
#
# This is a basic test of the mmap module. It is not exhaustive.


import sys
import os
import mmap
import unittest
from test import support

__missing__ = object()

class MmapTests(unittest.TestCase):

    def setUp(self):
        self.filename = support.TESTFN
        fd = os.open(self.filename, os.O_CREAT | os.O_RDWR)
        os.write(fd, b"1234567890")
        os.close(fd)
        self.file_size = 10
        self.map_size = mmap.PAGESIZE
        self.map_offset = 0
        self.map_mode = mmap.ACCESS_READ
        self.map_prot = mmap.PROT_READ
        self.map_pos = 0
        self.map_file = None
        self.map_tagname = None
        self.map_content_type = mmap.PAGESIZE * b"0"
        self.map_content_type_
