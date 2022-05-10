from types import FunctionType
list(FunctionType(func.__code__, globals(), 'foo').__globals__.items())

# Using a decorator
from decorator import decorator

@decorator
def trace(f, *args, **kw):
    print(f, args, kw)
    return f(*args, **kw)

@trace
def foo(a, b):
    return a + b

foo(1, 2)
