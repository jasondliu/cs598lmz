import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import os_helper

import io
import os
import sys
import tempfile
import weakref

# Base class for testing a RawIO implementation.
# Subclasses must override read(), seek(), tell() and close().
class BaseRawIOTest:
    # Constructor.  May be overridden, but subclasses should call
    # RawIOTest.__init__(self, *args).
    def __init__(self, *args):
        self.args = args

    # Utility methods.  May be overridden.
    def setUp(self):
        self.f = self.io.open(support.TESTFN, "w+b", *self.args)

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(support.TESTFN)

    def write_ops(self, s):
        self.f.write(s)
        self.f.seek(0)
        self.f.write(s)
        self
