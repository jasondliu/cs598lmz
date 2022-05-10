fn = lambda: None
# Test fn.__code__.co_varnames
def f(a, b):
    c = a + b
    d = a * b
    return c, d
f.__code__.co_varnames

# Test fn.__code__.co_argcount
f.__code__.co_argcount

# Test fn.__code__.co_argcount
def g(a, b=1):
    c = a + b
    d = a * b
    return c, d
g.__code__.co_argcount

# Test fn.__code__.co_argcount
def h(a, b, c=1, d=2, e=3):
    f = a + b + c + d + e
    g = a * b * c * d * e
    return f, g
h.__code__.co_argcount

# Test fn.__code__.co_argcount
def i(a, b, *args, **kwargs):
    c = a + b
    d = a * b
    return c, d
i.
