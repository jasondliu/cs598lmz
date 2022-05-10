import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert isinstance(float, types.BuiltinFunctionType)
assert isinstance(list, types.BuiltinFunctionType)
assert isinstance(dict, types.BuiltinFunctionType)
assert isinstance(set, types.BuiltinFunctionType)
assert isinstance(tuple, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(None, types.BuiltinFunctionType)
assert not isinstance(1, types.BuiltinFunctionType)
# Test types.GeneratorType
def g():
    yield 1

assert isinstance(g, types.Gener
