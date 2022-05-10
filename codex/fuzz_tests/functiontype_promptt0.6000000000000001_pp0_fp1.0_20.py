import types
# Test types.FunctionType
assert isinstance(len, types.FunctionType)
assert isinstance(abs, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(42, types.FunctionType)
assert not isinstance(3.14, types.FunctionType)
assert not isinstance('abc', types.FunctionType)
try:
    types.FunctionType
except NameError:
    pass
else:
    raise TestFailed, "types.FunctionType shouldn't be defined"

# Test types.LambdaType
assert not isinstance(len, types.LambdaType)
assert not isinstance(abs, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(int, types.LambdaType)
assert not isinstance(None, types.LambdaType)
assert not isinstance(42, types.LambdaType)
assert not isinstance(3.14, types.L
