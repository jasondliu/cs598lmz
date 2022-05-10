import types
# Test types.FunctionType

def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)

def g(x):
    return x

assert isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(g, types.MethodType)

def h(x, y):
    return x, y

assert isinstance(h, types.FunctionType)
assert not isinstance(h, types.BuiltinFunctionType)
assert not isinstance(h, types.MethodType)

def i(x, y, z):
    return x, y, z

assert isinstance(i, types.FunctionType)
assert not isinstance(i, types.BuiltinFunctionType)
assert not isinstance(i, types.MethodType)

def j(x, y, z, t):
    return x, y, z, t

assert isinstance(j, types.FunctionType)
assert
