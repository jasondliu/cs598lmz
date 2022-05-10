import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

# A mixin for RawIOBase tests that defines some utility methods
class RawIOMixin:
    # Utility functions

    def check_read_buffer_args(self, methname, *args):
        # Check that calling the given method with the given arguments
        # raises a TypeError.  The first argument is the object to call
        # the method on.
        meth = getattr(self.thetype, methname)
        self.assertRaises(TypeError, meth, *args)

    def check_write_buffer_args(self, methname, *args):
        # Check that calling the given method with the given arguments
        # raises a TypeError.  The first argument is the object to call
        # the method on.
        meth = getattr(self.thetype, methname)
        self.assertRaises(TypeError, meth, *args)

    def check_unsupported_operation(self, methname, *args):
        # Check that calling the given method with the
