import io
# Test io.RawIOBase
#
# This test checks that the io.RawIOBase() interface, which is used by
# io.FileIO, is implemented correctly.

import io
import os
import unittest
import tempfile
import struct
import sys
import pickle
import warnings
import errno

from test import support

TESTFN = support.TESTFN

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.fd = -1
        self.tempdir = None

    def tearDown(self):
        if self.fd > -1:
            os.close(self.fd)
        if self.tempdir:
            support.rmtree(self.tempdir)

    def open(self, **kwargs):
        support.unlink(TESTFN)
        self.fd = os.open(TESTFN, os.O_RDWR | os.O_CREAT)
        return io.FileIO(TESTFN, **kwargs)

    def test_read(self):
        f = self.open()
       
