import types
# Test types.FunctionType

def f():
    pass

assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)
assert type(lambda: None) == types.FunctionType
assert isinstance(lambda: None, types.FunctionType)
assert type(type) == types.BuiltinFunctionType
assert isinstance(type, types.BuiltinFunctionType)
assert type(int) == types.BuiltinFunctionType
assert isinstance(int, types.BuiltinFunctionType)
assert type(iter) == types.BuiltinFunctionType
assert isinstance(iter, types.BuiltinFunctionType)
# Test types.LambdaType

assert type((lambda: None)) == types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
assert type((lambda x: x)) == types.LambdaType
assert isinstance((lambda x: x), types.LambdaType)
assert type((lambda x, y, z: x + y + z)) == types.LambdaType
assert isinstance((lambda x, y, z: x + y + z
