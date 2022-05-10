import types
# Test types.FunctionType

def g(): pass
def f(x): return x

assert type(g) is types.FunctionType
assert type(f) is types.FunctionType
assert type(lambda: None) is types.FunctionType
assert type(lambda x: x) is types.FunctionType
assert type(lambda x, y: x) is types.FunctionType

assert type(f(1)) is types.FunctionType

assert not isinstance(f(1), types.FunctionType)
assert not isinstance(g, types.FunctionType)
assert not isinstance(f, types.FunctionType)
assert not isinstance(lambda: None, types.FunctionType)
assert not isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x, y: x, types.FunctionType)

assert not issubclass(f(1), types.FunctionType)
assert not issubclass(g, types.FunctionType)
assert not issubclass(f, types.FunctionType)
assert not issubclass(lambda: None, types.FunctionType)
assert not issubclass(lambda x
