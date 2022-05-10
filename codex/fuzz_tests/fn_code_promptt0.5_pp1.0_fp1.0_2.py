fn = lambda: None
# Test fn.__code__.co_name
def fn(): pass
print(fn.__code__.co_name)

# Test fn.__code__.co_argcount
def fn(a): pass
print(fn.__code__.co_argcount)

# Test fn.__code__.co_varnames
def fn(a): pass
print(fn.__code__.co_varnames)

# Test fn.__code__.co_code
def fn(a):
    b = 1
    c = 2
    return c
print(fn.__code__.co_code)

# Test fn.__code__.co_consts
def fn(a):
    b = 1
    c = 2
    return c
print(fn.__code__.co_consts)

# Test fn.__code__.co_names
def fn(a):
    b = 1
    c = 2
    return c
print(fn.__code__.co_names)

# Test fn.__code__.co_nlocals
def fn(a):
