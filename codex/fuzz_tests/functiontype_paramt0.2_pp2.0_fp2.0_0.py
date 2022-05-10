from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))

# Test that the function name is not interned
def f():
    pass
f.__name__ = 'a' * 100
list(FunctionType(lambda: None, globals(), f.__name__) for _ in range(10))

# Test that the function name is not interned
def f():
    pass
f.__name__ = 'a' * 100
list(FunctionType(lambda: None, globals(), f.__name__) for _ in range(10))

# Test that the function name is not interned
def f():
    pass
f.__name__ = 'a' * 100
list(FunctionType(lambda: None, globals(), f.__name__) for _ in range(10))

# Test that the function name is not interned
def f():
    pass
f.__name__ = 'a' * 100
list(FunctionType(lambda: None, globals(), f.__name__) for _ in range(10))

# Test that the function name is not
