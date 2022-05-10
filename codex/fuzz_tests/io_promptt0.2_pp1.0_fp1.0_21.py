import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import pickle
import _pyio as pyio

from test import support

# Base class for testing a RawIOBase implementation.
class BaseRawIOBaseTests(object):

    def test_constructor(self):
        # No public constructor
        self.assertRaises(TypeError, io.RawIOBase)

    def test_attributes(self):
        # No public constructor
        rawio = self.RawIO()
        self.assertRaises(io.UnsupportedOperation, getattr, rawio, 'name')
        self.assertRaises(io.UnsupportedOperation, getattr, rawio, 'mode')
        self.assertRaises(io.UnsupportedOperation, getattr, rawio, 'closed')

    def test_read(self):
        rawio = self.RawIO()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.read, 10
