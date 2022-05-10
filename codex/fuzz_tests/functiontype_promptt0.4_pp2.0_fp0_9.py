import types
# Test types.FunctionType
def f():
    pass

def g():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert f != g
assert f.__name__ == 'f'
assert g.__name__ == 'g'

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(min, types.BuiltinFunctionType)
assert isinstance(max, types.BuiltinFunctionType)
assert isinstance(ord, types.BuiltinFunctionType)
assert isinstance(chr, types.BuiltinFunctionType)
assert isinstance(bytearray, types.BuiltinFunctionType)
assert isinstance(bytes, types.BuiltinFunctionType)
assert isinstance(list, types.BuiltinFunctionType)
assert isinstance(tuple, types.BuiltinFunctionType)
assert isinstance(dict, types.BuiltinFunctionType)
assert isinstance(set, types.BuiltinFunctionType)
assert isinstance(frozenset, types.BuiltinFunctionType)
assert
