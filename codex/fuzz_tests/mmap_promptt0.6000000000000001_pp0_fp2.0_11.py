import mmap
# Test mmap.mmap.
# This test is based on the mmap test in the Python standard library test suite.
# It is modified to work on both Python 2 and 3 and to make sure that the
# mmap object is closed immediately when the object is deleted.
import mmap
import os
import stat
import sys
import tempfile
import unittest

import pytest


class MmapTests(unittest.TestCase):
    def setUp(self):
        self.tmpfile = tempfile.TemporaryFile()
        self.m = mmap.mmap(self.tmpfile.fileno(), 1024)

    def tearDown(self):
        self.m.close()
        self.tmpfile.close()

    def test_mmap(self):
        self.assertEqual(self.m.find(b'ciao'), -1)
        self.assertEqual(self.m.find(b'hello'), -1)
        self.assertEqual(self.m.find(b'hello world'), -1)

        self.m.write(b'hello world')
        self
