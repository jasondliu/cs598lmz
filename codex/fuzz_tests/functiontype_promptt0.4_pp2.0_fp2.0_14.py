import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(sum, types.BuiltinFunctionType)
assert isinstance(min, types.BuiltinFunctionType)
assert isinstance(max, types.BuiltinFunctionType)
assert isinstance(dict, types.BuiltinFunctionType)
assert isinstance(list, types.BuiltinFunctionType)
assert isinstance(tuple, types.BuiltinFunctionType)
assert isinstance(set, types.BuiltinFunctionType)
assert isinstance(str, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert isinstance(float, types.BuiltinFunctionType)
assert isinstance(bool, types.BuiltinFunctionType)
assert isinstance(bytearray, types.BuiltinFunctionType)
assert isinstance(bytes, types.BuiltinFunctionType)
assert isinstance(chr, types.BuiltinFunctionType)
assert isinstance(ord, types.Built
