import types
# Test types.FunctionType and types.BuiltinFunctionType
#
# This test is just a sanity check to make sure that the types
# are what we expect them to be.

import types

def test_function():
    assert type(test_function) is types.FunctionType
    assert type(len) is types.BuiltinFunctionType
    assert type(abs) is types.BuiltinFunctionType
    assert type(min) is types.BuiltinFunctionType
    assert type(max) is types.BuiltinFunctionType
