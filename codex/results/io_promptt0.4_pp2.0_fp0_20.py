import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
import weakref
from test import support
from test.support.script_helper import assert_python_ok

# A mixin class with utility methods
class IOTestBase:
    # Utility methods
    def assertRaisesWithMsg(self, excClass, msg, callableObj, *args, **kwargs):
        try:
            callableObj(*args, **kwargs)
        except excClass as exc:
            if str(exc) != msg:
                raise self.failureException("%s != %s" % (str(exc), msg))
        else:
            if hasattr(excClass, '__name__'): excName = excClass.__name__
            else: excName = str(excClass)
            raise self.failureException("%s not raised" % excName)

    def assertEqual(self, first, second, msg=None):
        if first != second:
            raise self.failureException(msg or "%r != %r" % (first, second))

    def assert
