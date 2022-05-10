import types
# Test types.FunctionType.

def f():
    pass

assert isinstance(f, types.FunctionType)

def g():
    return f

assert isinstance(g(), types.FunctionType)
