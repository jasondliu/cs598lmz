import types
# Test types.FunctionType
def f():
    pass

def g(x, y):
    pass

def h(x, y, z=1, *args):
    pass

def i(x, y, z=1, *args, **kw):
    pass

def j(x, y, z=1, *, k, **kw):
    pass

def k(x, y, z=1, *, k=2, **kw):
    pass

assert type(f) is types.FunctionType
assert type(g) is types.FunctionType
assert type(h) is types.FunctionType
assert type(i) is types.FunctionType
assert type(j) is types.FunctionType
assert type(k) is types.FunctionType

# Test types.LambdaType
lamb = lambda: None

assert type(lamb) is types.LambdaType

# Test types.GeneratorType
def gen():
    yield 1

assert type(gen()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__)
