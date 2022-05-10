import types
# Test types.FunctionType

def f():
    pass

assert type(f) == types.FunctionType
assert type(lambda: None) == types.FunctionType

def g(x):
    return x

def h(x):
    return x

assert g is not h
assert type(g) == type(h)

# Test isinstance() on builtin types

assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert isinstance(h, types.FunctionType)

# Test types.LambdaType

assert type(lambda: None) == types.LambdaType

def g():
    return lambda: None

assert type(g()) == types.LambdaType

# Test types.GeneratorType

def f():
    yield 1

assert type(f()) == types.GeneratorType

# Test types.CodeType

# This is a little hacky, but it does work...
assert type(f.__code__) == types.CodeType

# Test types.MethodType

class C(object
