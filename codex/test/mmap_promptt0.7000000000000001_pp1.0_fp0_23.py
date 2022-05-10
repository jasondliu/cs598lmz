import mmap
# Test mmap.mmap(fileno, length, tagname, access=mmap.ACCESS_WRITE)
#
# This test focuses on the access parameter.
#
# Try to mmap a file in different modes and ensure that the correct
# memory is written.
#
# Written by: Karl Vietmeier

import unittest
import os
import mmap
import tempfile

class mmap_writeTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = tempfile.mktemp()
        self.file = open(self.filename, "wb+")

    def tearDown(self):
        self.file.close()
        os.unlink(self.filename)

    def do_mmap(self, length, access):
        self.file.seek(0)
        self.file.truncate()
        self.file.write(b"\x00" * length)
        self.file.flush()
        self.file.seek(0)
        m = mmap.mmap(self.file.fileno(), length, access=access)
