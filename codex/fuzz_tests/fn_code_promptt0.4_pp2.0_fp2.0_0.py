fn = lambda: None
# Test fn.__code__.co_varnames
def func(a, b, c):
    pass

print(func.__code__.co_varnames)

# Test fn.__code__.co_argcount
def func(a, b, c):
    pass

print(func.__code__.co_argcount)

# Test fn.__code__.co_nlocals
def func(a, b, c):
    pass

print(func.__code__.co_nlocals)

# Test fn.__code__.co_stacksize
def func(a, b, c):
    pass

print(func.__code__.co_stacksize)

# Test fn.__code__.co_flags
def func(a, b, c):
    pass

print(func.__code__.co_flags)

# Test fn.__code__.co_consts
def func(a, b, c):
    pass

print(func.__code__.co_consts)

# Test fn.__code
