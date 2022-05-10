import types
# Test types.FunctionType using a custom function as well as a lambda.
assert type(lambda x: x) == types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
def f(x): return x
assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType using a custom function as well as a lambda.
try:
    import _testcapi
    # Check if _testcapi has the builtin_sum function.
    assert hasattr(_testcapi, "builtin_sum")
except ImportError:
    # Skip the test if _testcapi doesn't exist.
    pass
else:
    assert type(_testcapi.builtin_sum) == types.BuiltinFunctionType
    assert isinstance(_testcapi.builtin_sum, types.BuiltinFunctionType)
    assert type(lambda x: x) == types.FunctionType
    assert isinstance(lambda x: x, types.FunctionType)
    assert type(sum) == types.BuiltinFunctionType
    assert isinstance(sum,
