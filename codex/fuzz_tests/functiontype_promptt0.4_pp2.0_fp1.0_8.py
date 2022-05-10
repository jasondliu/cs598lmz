import types
# Test types.FunctionType and types.MethodType
#
# This test is not intended to be exhaustive.  It just checks that
# types.FunctionType and types.MethodType are defined, and that they are
# subclasses of types.BuiltinFunctionType and types.BuiltinMethodType.

import types

def test_function_type():
    assert issubclass(types.FunctionType, types.BuiltinFunctionType)

def test_method_type():
    assert issubclass(types.MethodType, types.BuiltinMethodType)
