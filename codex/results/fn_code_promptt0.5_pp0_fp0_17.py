fn = lambda: None
# Test fn.__code__.co_varnames
def f():
    a = 1
    b = 2
    c = 3
    return a + b + c
f.__code__.co_varnames

# Test fn.__code__.co_argcount
def f(a, b, c):
    return a + b + c
f.__code__.co_argcount

# Test fn.__code__.co_stacksize
def f(a, b, c, d, e, f, g):
    return a + b + c + d + e + f + g
f.__code__.co_stacksize

# Test fn.__code__.co_flags
def f(a, b, c):
    return a + b + c
f.__code__.co_flags

# Test fn.__code__.co_consts
def f():
    return 1 + 2 + 3
f.__code__.co_consts

# Test fn.__code__.co_names
def f():
    return c
f.__code__.
