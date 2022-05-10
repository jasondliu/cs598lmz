fn = lambda: None
# Test fn.__code__.co_varnames

def f():
    a = 1
    b = 2
    c = 3

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_varnames

def f(a, b, c):
    pass

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_varnames

def f(a, b, c=1):
    pass

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_varnames

def f(a, b, c=1, *args):
    pass

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_varnames
