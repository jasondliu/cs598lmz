import types
# Test types.FunctionType
#
# This test is derived from the test_types test from the Python 2.6
# library test suite.
#
# The original Python 2.6 test_types test was written by Mark Hammond.
#
# The original Python 2.6 test_types test was modified by Bob Ippolito to
# test Jython-specific behavior.

import unittest
from test import test_support

class TypesTestCase(unittest.TestCase):

    def test_types(self):
        # Test the types module.

        self.assert_(types.FunctionType is type(lambda: None))

        self.assert_(types.BuiltinFunctionType is type(len))
        self.assert_(types.BuiltinFunctionType is type(min))
        self.assert_(types.BuiltinFunctionType is type(pow))
        self.assert_(types.BuiltinFunctionType is type(str.strip))

        self.assert_(types.MethodType is type(str.strip))

        self.assert_(types.UnboundMethodType is type(str.strip))

        # self.assert_(types.
