import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda: 0, types.FunctionType)
assert isinstance(lambda x, y: x+y, types.FunctionType)
assert isinstance(lambda **x: x, types.FunctionType)
assert isinstance(lambda *x: x, types.FunctionType)
assert isinstance(lambda x, *y: x+y, types.FunctionType)
assert isinstance(lambda x, **y: x+y, types.FunctionType)
assert isinstance(lambda x, *y, **z: x+y+z, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(min, types.BuiltinFunctionType)
assert isinstance(hash, types.BuiltinFunctionType)

# Test type.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert isinstance(lambda: 0, types.LambdaType)
assert isinstance(lambda x, y: x+y, types.LambdaType)
assert isinstance(lambda **x
