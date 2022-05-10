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

# Base class for testing a RawIOBase implementation.
# Subclasses must override read(), readall() and write().
class BaseRawIOBaseTests(object):

    def setUp(self):
        self.f = self.IOCls(self.TESTFN, "w+b")
        self.f.close()
        self.f = self.IOCls(self.TESTFN, "w+b")

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(self.TESTFN)

    def test_attributes(self):
        self.assertTrue(hasattr(self.f, 'name'))
        self.assertTrue(hasattr(self.f, 'mode'))
        self.assertTrue(hasattr(self.f, 'closed'))
        self.assertTrue(hasattr(self.f,
