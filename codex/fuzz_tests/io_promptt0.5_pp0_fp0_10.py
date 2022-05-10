import io
# Test io.RawIOBase
#
# This tests the RawIOBase implementation of the io module.  Since
# RawIOBase is a base class, the tests are performed by creating a
# number of derived classes.
#
# Note that RawIOBase derives from IOBase, which is tested in test_io.
# The tests for open(), close(), seek(), tell(), truncate(), read(),
# readinto(), write() and detach() are therefore not repeated here.

import io
import os
import sys
import tempfile
import unittest
from io import BytesIO, StringIO
from test import support
from test.support import TESTFN, run_unittest, import_module

# A couple of standard errors we can use to validate exception handling
ERROR1 = OSError()
ERROR2 = ValueError()

class AutoFileTests(unittest.TestCase):
    # file tests for which a (writable) file is automatically set up

    def setUp(self):
        self.f = open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:

