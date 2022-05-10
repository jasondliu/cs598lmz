from types import FunctionType
list(FunctionType(lambda : 1, globals(), "lambda"))

# Test function attributes
def f():
    pass

f.foo = 1
f.foo

# Test function annotations
def f(x: int):
    return x

f.__annotations__

# Test function annotations with defaults
def f(x: int = 1):
    return x

f.__annotations__

# Test function annotations with *args
def f(*args: int):
    return args

f.__annotations__

# Test function annotations with **kwargs
def f(**kwargs: int):
    return kwargs

f.__annotations__

# Test function annotations with *args and **kwargs
def f(*args: int, **kwargs: int):
    return args, kwargs

f.__annotations__

# Test function annotations with *args and defaults
def f(*args: int, x: int = 1):
    return args, x

f.__annotations__

# Test function annotations with **kwargs and defaults
def f(**kwargs:
