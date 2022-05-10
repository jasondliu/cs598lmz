fn = lambda: None
# Test fn.__code__.co_varnames
def f1():
    a = 1
    b = 2
    c = 3
    return a + b + c

# Test fn.__code__.co_argcount
def f2(a, b, c):
    return a + b + c

# Test fn.__code__.co_argcount with default args
def f3(a, b=2, c=3):
    return a + b + c

# Test fn.__code__.co_argcount with kwargs
def f4(a, b=2, c=3, **kwargs):
    return a + b + c

# Test fn.__code__.co_argcount with args and kwargs
def f5(a, b=2, c=3, *args, **kwargs):
    return a + b + c

# Test fn.__code__.co_argcount with kwonlyargs
def f6(a, b=2, c=3, *, d, **kwargs):
    return a + b + c + d

