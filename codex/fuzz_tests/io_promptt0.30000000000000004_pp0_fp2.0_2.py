import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import _io

# The io module is a wrapper around _io, which is written in C.  The
# _io module provides a C API that is used by the io module.  The
# _io module also provides a Python API, which is used by the test
# suite.

class BaseTestRawIO(object):

    def test_read(self):
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(1), b'x')
        self.assertEqual(self.io.read(10), b'x'*10)
        self.assertEqual(self.io.read(1), b'')

    def test_readall(self):
        self.assertEqual(self.io.readall(), b'x'*100)
        self.assertEqual(self.io.readall(), b'')

    def test_readinto(self):
        b = bytear
