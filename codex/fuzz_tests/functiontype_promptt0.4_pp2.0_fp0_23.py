import types
# Test types.FunctionType

def f():
    ...

assert isinstance(f, types.FunctionType)

def f(x, y):
    ...

assert isinstance(f, types.FunctionType)

def f(x, y, *, z):
    ...

assert isinstance(f, types.FunctionType)

def f(x, y, *args, z):
    ...

assert isinstance(f, types.FunctionType)

def f(x, y, *args, z, **kwargs):
    ...

assert isinstance(f, types.FunctionType)


def f(x, y, *, z=1):
    ...

assert isinstance(f, types.FunctionType)

def f(x, y, *args, z=1):
    ...

assert isinstance(f, types.FunctionType)

def f(x, y, *args, z=1, **kwargs):
    ...

assert isinstance(f, types.FunctionType)

def f(x, y, *, z=1, **kw
