import io
# Test io.RawIOBase.readinto()

import os
import sys
import unittest
from test import support
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRWPair, \
        BufferedRandom, TextIOWrapper
from _io import DEFAULT_BUFFER_SIZE

def check_size(f, size):
    # Check that a file has the given size.
    f.seek(0, 2)                 # seek to end of file
    if f.tell() != size:
        raise RuntimeError("file has wrong size")

class TestRawIOBase(unittest.TestCase):

    def setUp(self):
        # Base class for testing io.RawIOBase.
        # A concrete test class must override read(), write(), seek(),
        # and seekable().
        self.f = self.FileIO(support.TESTFN, "w+b")

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(support.TESTFN)

    def test_rawiobase(self
