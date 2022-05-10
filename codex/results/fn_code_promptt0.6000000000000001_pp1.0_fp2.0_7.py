fn = lambda: None
# Test fn.__code__.co_argcount
assert fn.__code__.co_argcount == 0
assert fn.__code__.co_argcount == fn.__code__.co_nlocals

# Test fn.__code__.co_kwonlyargcount
def fn(*, a):
    pass
assert fn.__code__.co_kwonlyargcount == 1

# Test fn.__code__.co_varnames
def fn(a, b, c, d):
    pass
assert fn.__code__.co_varnames == ('a', 'b', 'c', 'd')

# Test fn.__code__.co_argcount
assert fn.__code__.co_argcount == 4
assert fn.__code__.co_argcount == fn.__code__.co_nlocals

# Test fn.__code__.co_kwonlyargcount
def fn(*, a):
    pass
assert fn.__code__.co_kwonlyargcount == 1

# Test fn.__code__.co_varnames
def fn(a
