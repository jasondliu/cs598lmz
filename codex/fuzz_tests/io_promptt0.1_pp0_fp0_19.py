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
class BaseRawIOSharingTests:
    # The name of the implementation
    name = None
    # The type object of the implementation
    type2test = None
    # A template for creating file objects
    template = None

    def setUp(self):
        # Create a file for testing
        f = open(TESTFN, 'wb')
        try:
            f.write(b'abcdefghijklmnop'*4)
        finally:
            f.close()
        self.f = open(TESTFN, 'rb')

    def tearDown(self):
        if self.f:
            self.f.close()
        un
