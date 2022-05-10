from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that we can create a function with a non-string name
def f():
    pass
f.__name__ = 42
list(FunctionType(f.__code__, globals(), f.__name__))

# Test that we can create a function with a non-string docstring
def f():
    pass
f.__doc__ = 42
list(FunctionType(f.__code__, globals(), f.__name__, f.__doc__))

# Test that we can create a function with a non-string module
def f():
    pass
f.__module__ = 42
list(FunctionType(f.__code__, globals(), f.__name__, f.__doc__, f.__module__))

# Test that we can create a function with a non-string dict
def f():
    pass
f.__dict__ = 42
list(FunctionType(f.__code__, globals(), f.__name__, f.__doc__, f.__module__, f.__dict__
