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
# and set the class attributes name and description.

class BaseRawIO(object):

    def setUp(self):
        self.f = self.IOCls(TESTFN, "w+b")

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_attributes(self):
        self.assertEqual(self.f.mode, "w+b", "invalid mode")
        self.assertEqual(self.f.name, TESTFN, "invalid name")
        self.assertEqual(self.f.closed, False, "closed not False")

    def test_weakref(self):
        p
