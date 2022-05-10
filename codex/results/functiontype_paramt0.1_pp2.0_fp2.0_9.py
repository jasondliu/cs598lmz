from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for i in range(2))

# Test that the function name is not interned.
def f():
    pass
f.__name__ = 'foo'
list(FunctionType(lambda: None, globals(), f.__name__) for i in range(2))

# Test that the function name is not interned.
def f():
    pass
f.__name__ = 'foo'
list(FunctionType(lambda: None, globals(), f.__name__) for i in range(2))

# Test that the function name is not interned.
def f():
    pass
f.__name__ = 'foo'
list(FunctionType(lambda: None, globals(), f.__name__) for i in range(2))

# Test that the function name is not interned.
def f():
    pass
f.__name__ = 'foo'
list(FunctionType(lambda: None, globals(), f.__name__) for i in range(2))

# Test that the function name is not interned.

