import io
# Test io.RawIOBase
import io
import unittest
import sys
import os
import tempfile
import weakref
import errno
import _pyio as pyio

class BaseTestRawIO(object):

    def test_abstract_methods(self):
        # File-like objects have various methods that are not tested here
        # because they are implementation details.  The tests for these
        # methods are in the concrete subclasses.
        #
        # This test makes sure that the abstract methods are actually
        # abstract.  If they are not, then the concrete subclasses will
        # not override them, and this test will fail.
        with self.assertRaises(io.UnsupportedOperation):
            self.io.read(0)
        with self.assertRaises(io.UnsupportedOperation):
            self.io.write(b"")
        with self.assertRaises(io.UnsupportedOperation):
            self.io.seek(0)
        with self.assertRaises(io.UnsupportedOperation):
            self.io.tell()
        with self.assertRaises(io.Unsupported
