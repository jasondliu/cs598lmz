fn = lambda: None
# Test fn.__code__.co_varnames
def f():
    a = 1
    b = 2
    c = 3
    return a + b + c

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount
def f(a, b, c):
    return a + b + c

print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount
def f(*args):
    return args

print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount
def f(**kwargs):
    return kwargs

print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount
def f(a, b, c, *args, **kwargs):
    return a + b + c + args + kwargs

print(f.__code__.co_argcount)

#
