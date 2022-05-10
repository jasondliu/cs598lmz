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
from test.support import TESTFN, unlink

# Base class for testing a RawIO implementation.
# Subclasses must override read(), readall() and seek(),
# and set the class attributes name, type2test and template.
class BaseRawIOSharingTests:
    # The name of the test class
    name = None
    # The type to be tested
    type2test = None
    # A template for creating the test object
    template = None

    def setUp(self):
        self.f = self.type2test(self.template)

    def tearDown(self):
        self.f.close()

    def test_attributes(self):
        self.assertEqual(self.f.mode, "rb",
                         "%s: bad mode: %r" % (self.name, self.f.mode))
        self.assertEqual(self.f.name, self.template,
