import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import _pyio as pyio

from test import support
from test.support import TESTFN, unlink, run_unittest

# Base class for testing a RawIO implementation.
# Subclasses must override read(), readall() and seek(),
# and set the class attributes name, type2test and template.
class BaseTestRawIO(object):
    name = None
    type2test = None
    template = None

    def setUp(self):
        # Create a test file
        f = open(TESTFN, 'wb')
        f.write(self.template)
        f.close()
        self.f = open(TESTFN, 'rb')
        self.r = self.type2test(self.f)

    def tearDown(self):
        self.r.close()
        self.f.close()
        unlink(TESTFN)

    def test_attributes(self):
        self.assertEqual(self.r.
