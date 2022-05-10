import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)

# Test types.MethodType
assert isinstance(f.__call__, types.MethodType)
assert not isinstance(f.__call__, types.FunctionType)
assert not isinstance(f.__call__, types.BuiltinFunctionType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert not isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x: x, types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.MethodType)

# Test types.GeneratorType
assert isinstance((x for x in range(
