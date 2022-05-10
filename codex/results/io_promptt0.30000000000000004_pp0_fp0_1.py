import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno

from test import test_support
from test.test_support import TESTFN, run_unittest, import_module

# Base class for testing io.RawIOBase.
#
# Subclasses must define a read() method.
#
# The read() method is called with a byte string argument, and should
# return a byte string.  The argument will be of the correct length,
# unless the end of the "file" is reached, in which case it will be
# zero length.
#
# setUp() creates a RawIO object using the object returned by
# open_raw_io() (a RawIOBase object), and stores it as self.the_raw_io.
# Various tests are then performed on self.the_raw_io using the check_*()
# methods.
#
# tearDown() closes self.the_raw_io, and sets it to None.
#
# Subclasses should feel free to add other tests.

class BaseRawIOTest(un
