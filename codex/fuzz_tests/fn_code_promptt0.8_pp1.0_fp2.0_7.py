fn = lambda: None
# Test fn.__code__.co_argcount
@dist / fn.__code__.co_argcount
def foo(x, y):
    return x + y

assert foo(1, 2).result() == 3

# Test fn.__code__.co_varnames
@dist / fn.__code__.co_varnames
def foo(x, y):
    return [x, y]

assert foo(1, 2).result() == [1, 2]

# Test fn.__code__.co_varnames
@dist / fn.__code__.co_varnames
def foo(x, y, z=None):
    return [x, y, z]

assert foo(1, 2).result() == [1, 2, None]

# Test fn.__code__.co_varnames
@dist / fn.__code__.co_varnames
def foo(x, y, z=None):
    return [x, y, z]

assert foo(1, 2, z=3).result() == [1, 2, 3]
