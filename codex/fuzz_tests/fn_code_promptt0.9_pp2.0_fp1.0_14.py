fn = lambda: None
# Test fn.__code__.co_varnames
x = fn()
print(fn.__code__.co_varnames)

# Test fn.__code__.co_consts
print(fn.__code__.co_consts)

# Test fn.__code__.co_argcount
print(fn.__code__.c
