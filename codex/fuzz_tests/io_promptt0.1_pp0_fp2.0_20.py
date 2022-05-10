import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings
from test import support
from test.support import import_module

# Skip tests if there is no os.sendfile()
sendfile = import_module('sendfile')

# Skip tests if there is no os.sendfile()
sendfile = import_module('sendfile')

class TestRawIOBase(unittest.TestCase):

    def test_constructor(self):
        # No constructor test needed, as io.RawIOBase is an abstract class.
        pass

    def test_read(self):
        # read() is tested in RawIOBaseTest.
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        # readinto() is tested in RawIOBaseTest.
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_write(self):
        # write() is tested in RawIO
