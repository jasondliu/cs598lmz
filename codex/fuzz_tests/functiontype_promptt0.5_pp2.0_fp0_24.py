import types
# Test types.FunctionType, types.LambdaType, types.CodeType, types.MethodType

# Test FunctionType

def f(): pass

assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)
assert not issubclass(types.FunctionType, types.LambdaType)
assert not issubclass(types.FunctionType, types.CodeType)
assert not issubclass(types.FunctionType, types.MethodType)

# Test LambdaType

l = lambda: 1

assert type(l) == types.LambdaType
assert isinstance(l, types.LambdaType)
assert not issubclass(types.LambdaType, types.FunctionType)
assert not issubclass(types.LambdaType, types.CodeType)
assert not issubclass(types.LambdaType, types.MethodType)

# Test CodeType

assert type(f.__code__) == types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert not issubclass(types.CodeType,
