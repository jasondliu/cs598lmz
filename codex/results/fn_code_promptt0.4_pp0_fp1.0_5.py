fn = lambda: None
# Test fn.__code__
print(fn.__code__)
# Test fn.__code__.co_code
print(fn.__code__.co_code)
# Test fn.__code__.co_consts
print(fn.__code__.co_consts)
# Test fn.__code__.co_varnames
print(fn.__code__.co_varnames)
# Test fn.__code__.co_names
print(fn.__code__.co_names)
# Test fn.__code__.co_argcount
print(fn.__code__.co_argcount)
# Test fn.__code__.co_nlocals
print(fn.__code__.co_nlocals)
# Test fn.__code__.co_stacksize
print(fn.__code__.co_stacksize)
# Test fn.__code__.co_flags
print(fn.__code__.co_flags)
# Test fn.__code__.co_firstlineno
print(fn.__code__.co_firstlineno)

