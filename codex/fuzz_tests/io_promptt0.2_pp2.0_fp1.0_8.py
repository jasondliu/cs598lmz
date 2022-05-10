import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# A mixin class to provide tests common to RawIOBase and BufferedIOBase.
class BaseRawIOBaseTest(object):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.io.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, bytearray())

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readall)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.io.write, b'')

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.io.seek, 0)

    def test_tell(self):
        self.assertRaises(io.UnsupportedOperation, self.io.tell)

   
