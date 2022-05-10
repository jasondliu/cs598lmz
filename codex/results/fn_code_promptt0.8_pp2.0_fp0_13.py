fn = lambda: None
# Test fn.__code__.co_firstlineno
setattr(fn, "__code__", lambda: None)
setattr(fn.__code__, "co_firstlineno", 123)

# Test fn.__code__.co_firstlineno
setattr(fn, "__code__", lambda: None)
setattr(fn.__code__, "co_firstlineno", lambda: None)
setattr(fn.__code__.co_firstlineno, "x", 123)


# Test f(p, *args)
q = lambda x=1, y=2: x + y
q(2, 3)


def f1(a, b, c):
    return a + b + c


def f1(a, b, c, d, **kwargs):
    pass


def f2(a, b, c, d, e, f):
    pass


def f3(a, b, c, d, e, f, g):
    pass


def f4(a, b, c, d, e, f, g, h):
    pass
