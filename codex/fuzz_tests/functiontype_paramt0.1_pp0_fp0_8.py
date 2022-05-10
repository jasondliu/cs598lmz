from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that we can create a function with a non-string name
def f():
    pass
f.__name__ = 42
FunctionType(f.__code__, globals(), 42)

# Test that we can create a function with a non-string docstring
def f():
    pass
f.__doc__ = 42
FunctionType(f.__code__, globals(), 'foo', 42)

# Test that we can create a function with a non-string module
def f():
    pass
f.__module__ = 42
FunctionType(f.__code__, globals(), 'foo', 'foo', 42)

# Test that we can create a function with a non-string dict
def f():
    pass
f.__dict__ = 42
FunctionType(f.__code__, globals(), 'foo', 'foo', 'foo', 42)

# Test that we can create a function with a non-string closure
def f():
    pass
f.__closure__ = 42
FunctionType(f.__code__,
