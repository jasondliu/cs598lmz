import types
# Test types.FunctionType

def func(c):
    return c + 12

assert isinstance(func, types.FunctionType), 'Expected function to be types.FunctionT
