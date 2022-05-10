import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
def f(a, b, c):
    pass
assert isinstance(f, types.FunctionType)
def f(a, b, c=1):
    pass
assert isinstance(f, types.FunctionType)
def f(a, b, c=1, *args):
    pass
assert isinstance(f, types.FunctionType)
def f(a, b, c=1, *args, **kw):
    pass
assert isinstance(f, types.FunctionType)
def f(a, b, c=1, *args, **kw):
    yield 1
assert isinstance(f, types.FunctionType)
def f(a, b, c=1, *args, **kw):
    yield 1
    return 1
assert isinstance(f, types.FunctionType)
def f(a, b, c=1, *args, **kw):
    yield 1
    return 1
    yield 2
assert isinstance(f, types.FunctionType)
def f(a, b
