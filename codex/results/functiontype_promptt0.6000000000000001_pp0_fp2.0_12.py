import types
# Test types.FunctionType

def f(x):
    return x

assert(isinstance(f, types.FunctionType))
assert(f(42) == 42)
