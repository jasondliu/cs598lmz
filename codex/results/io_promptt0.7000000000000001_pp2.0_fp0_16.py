import io
# Test io.RawIOBase, io.BufferedIOBase, io.TextIOBase

import os
import struct
import sys
import tempfile
import unittest
from test import support
from test.support import import_helper
from test.support import run_unittest
from test.support import TESTFN
from test.support.script_helper import assert_python_ok, assert_python_failure

# A Mixin class with various methods that are useful for different types
# of IOBase objects.  Also ensures that the object on which the tests
# are run has the attributes we expect.
class IOBaseTestsMixin(object):
    # The class to instantiate for testing.
    ioclass = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.ioclass, 'mode'))
        self.assertTrue(hasattr(self.ioclass, 'name'))

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.ioclass().read)

    def test_readinto(self):

