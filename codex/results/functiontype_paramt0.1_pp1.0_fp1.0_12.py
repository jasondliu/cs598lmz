from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that we can create a function with a non-string name
def f():
    pass
f.__name__ = 42
list(f)

# Test that we can create a function with a non-string docstring
def f():
    pass
f.__doc__ = 42
list(f)

# Test that we can create a function with a non-string module
def f():
    pass
f.__module__ = 42
list(f)

# Test that we can create a function with a non-string dict
def f():
    pass
f.__dict__ = 42
list(f)

# Test that we can create a function with a non-string qualname
def f():
    pass
f.__qualname__ = 42
list(f)

# Test that we can create a function with a non-string default values
def f(a=42):
    pass
list(f)

# Test that we can create a function with a non-string annotations
def f(a: 42):
    pass

