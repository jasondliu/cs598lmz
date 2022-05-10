import types
# Test types.FunctionType
def func(): pass

assert type(func) is types.FunctionType
assert isinstance(func, types.FunctionType)

assert type(lambda x: x) is types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)

assert type(map) is types.BuiltinFunctionType
assert isinstance(map, types.BuiltinFunctionType)

assert type(min) is types.BuiltinFunctionType
assert isinstance(min, types.BuiltinFunctionType)

assert type(max) is types.BuiltinFunctionType
assert isinstance(max, types.BuiltinFunctionType)

assert type(abs) is types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

assert type(pow) is types.BuiltinFunctionType
assert isinstance(pow, types.BuiltinFunctionType)

assert type(round) is types.BuiltinFunctionType
assert isinstance(round, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert type(object.__init__) is types.BuiltinMethod
