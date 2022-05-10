import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert type(f) is types.FunctionType
assert type(f) == types.FunctionType
assert type(f) is not types.BuiltinFunctionType
assert type(f) != types.BuiltinFunctionType
assert type(f) is not types.BuiltinMethodType
assert type(f) != types.BuiltinMethodType
assert type(f) is not types.MethodType
assert type(f) != types.MethodType
assert type(f) is not types.LambdaType
assert type(f) != types.LambdaType
assert type(f) is not types.GeneratorType
assert type(f) != types.GeneratorType

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert type(len) is types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) is not types.FunctionType
assert type(len) != types.FunctionType
assert type(len) is not types.BuiltinMethodType
