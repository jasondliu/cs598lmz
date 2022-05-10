fn = lambda: None
# Test fn.__code__.co_varnames

def f():
    x = 1
    y = 2
    z = 3
    return x + y + z

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount

def f(x, y, z):
    return x + y + z

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount

def f(x, y, z, *args):
    return x + y + z

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount

def f(x, y, z, *args, **kwargs):
    return x + y + z

print(f.__code__.co_varnames)
print(f.__
