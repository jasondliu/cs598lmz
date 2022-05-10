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

def f(a, b, c=1, **kwargs):
    pass
assert isinstance(f, types.FunctionType)

def f(a, b, c=1, *args, **kwargs):
    pass
assert isinstance(f, types.FunctionType)

def f(a, b, c, *, d, e=1):
    pass
assert isinstance(f, types.FunctionType)

def f(a, b, c, *, d, e=1, **kwargs):
    pass
assert isinstance(f, types.FunctionType)

def f(*args):
    pass
assert
