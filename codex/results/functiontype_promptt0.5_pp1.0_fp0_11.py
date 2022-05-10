import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert type(lambda x: x) == types.FunctionType
assert type(lambda **kw: None) == types.FunctionType
assert type(lambda *args: None) == types.FunctionType
assert type(lambda *args, **kw: None) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType
assert type(type) == types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(int) == types.BuiltinFunctionType
assert type(str) == types.BuiltinFunctionType
assert type(object) == types.BuiltinFunctionType
assert type(range) == types.BuiltinFunctionType
assert type(bytearray) == types.BuiltinFunctionType
assert type(iter) == types.BuiltinFunctionType
assert type(next) == types.BuiltinFunctionType
assert type(reversed) == types.BuiltinFunctionType
assert type(dict.values) == types.BuiltinMethodType
assert
