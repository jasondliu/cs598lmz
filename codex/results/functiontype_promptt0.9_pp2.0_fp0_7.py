import types
# Test types.FunctionType and types.LambdaType for user-defined functions and lambdas.
# This should actually run Python 2.5 on py3k.

import sys
import unittest
from test import test_support
import weakref

class TypesTests(unittest.TestCase):

    def test_function_type(self):

        def function(): pass

        self.assert_(type(function) is types.FunctionType)
        self.assert_(type(lambda x: x) is types.FunctionType)
        self.assert_(type(FunctionType) is types.FunctionType)
        self.assertRaises(TypeError, type, function,
                          (types.FunctionType, types.FunctionType), {})

    def test_lambda_type(self):
        self.assert_(type(lambda:None) is types.LambdaType)

    def test_method_type(self):
        self.assert_(type([].append) is types.MethodType)

    def test_builtin_type(self):
        self.assert_(type(len) is types.BuiltinFunctionType)
