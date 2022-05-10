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
# Subclasses must override read(), readinto() and seek().
class BaseRawIOBaseTests(object):

    def test_constructor(self):
        # No public constructor.
        self.assertRaises(TypeError, io.RawIOBase)

    def test_attributes(self):
        # readinto()
        self.assertTrue(hasattr(self.IOClass, 'readinto'))
        self.assertTrue(callable(self.IOClass.readinto))
        # readall()
        self.assertTrue(hasattr(self.IOClass, 'readall'))
        self.assertTrue(callable(self.IOClass.readall))
        # read()
        self.assertTrue(hasattr(self.IOClass, 'read'))
        self.assertTrue(callable(self.IOClass.read))
        #
