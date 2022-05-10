fn = lambda: None
# Test fn.__code__.co_filename, fn.__code__.co_firstlineno
def test_fn():
    pass
test_fn.__code__.co_filename
test_fn.__code__.co_firstlineno

# Test fn.__code__.co_varnames
def test_fn2(a, b, c):
    x = 1
    y = 2
    z = 3
    return x + y + z
test_fn2.__code__.co_varnames
test_fn2.__code__.co_argcount

# Test fn.__code__.co_varnames
def test_fn3(a, b, c, *args, **kwargs):
    x = 1
    y = 2
    z = 3
    return x + y + z
test_fn3.__code__.co_varnames
test_fn3.__code__.co_argcount

# Test fn.__code__.co_varnames
def test_fn4(a, b, c):
    x = 1
    y =
