from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# Test that the __call__ method of a function can be used to invoke the
# function.
def foo():
    return 'foo'

list(foo.__call__())

# Test that the __call__ method of a function can be used to invoke the
# function with parameters.
def foo(x):
    return x

list(foo.__call__(42))

# Test that the __call__ method of a function can be used to invoke the
# function with parameters and keyword arguments.
def foo(x, y=1):
    return x, y

list(foo.__call__(x=42))

# Test that the __call__ method of a function can be used to invoke the
# function with parameters and keyword arguments.
def foo(x, y=1):
    return x, y

list(foo.__call__(42, y=2))

# Test that the __call__ method of a function can be used to invoke the
# function with parameters and keyword arguments.
def foo(x, y=
