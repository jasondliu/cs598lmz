from types import FunctionType
list(FunctionType(a, globals(), 'name'))

# Test that we don't have a __new__ on the type.
try:
    FunctionType.__new__(FunctionType, a, globals())
except TypeError:
    pass
else:
    raise Exception('should have raised a TypeError')


# Test that we can create a function with a __dict__
def f(x):
    return x
f.__dict__['x'] = 1
FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)

# Test that we can create a function with a __dict__
def f(x):
    return x
f.__dict__['x'] = 1
FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__, f.__dict__)

# Test that we can create a function with a __doc__
def f(x):
    return x
f.__doc__ = 'h
