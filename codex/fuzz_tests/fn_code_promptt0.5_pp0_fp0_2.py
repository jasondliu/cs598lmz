fn = lambda: None
# Test fn.__code__.co_varnames
def func(a, b, c):
    pass

print(func.__code__.co_varnames)

# Test fn.__code__.co_argcount
print(func.__code__.co_argcount)

# Test fn.__code__.co_filename
print(func.__code__.co_filename)

# Test fn.__code__.co_firstlineno
print(func.__code__.co_firstlineno)

# Test fn.__code__.co_consts
print(func.__code__.co_consts)

# Test fn.__code__.co_names
print(func.__code__.co_names)

# Test fn.__code__.co_nlocals
print(func.__code__.co_nlocals)

# Test fn.__code__.co_stacksize
print(func.__code__.co_stacksize)

# Test fn.__code__.co_flags
print(func.__code__.
