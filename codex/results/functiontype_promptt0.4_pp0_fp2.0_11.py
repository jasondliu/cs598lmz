import types
# Test types.FunctionType

def f():
    pass

def g():
    pass

def h():
    pass

assert type(f) is types.FunctionType
assert type(g) is types.FunctionType
assert type(h) is types.FunctionType

assert type(f) == type(g)
assert type(f) == type(h)
assert type(g) == type(h)

assert f.__class__ is types.FunctionType
assert g.__class__ is types.FunctionType
assert h.__class__ is types.FunctionType

assert f.__class__ == g.__class__
assert f.__class__ == h.__class__
assert g.__class__ == h.__class__

# Test types.LambdaType

l = lambda: None

assert type(l) is types.LambdaType
assert type(l) == types.LambdaType
assert l.__class__ is types.LambdaType
assert l.__class__ == types.LambdaType

# Test types.GeneratorType

def g():
