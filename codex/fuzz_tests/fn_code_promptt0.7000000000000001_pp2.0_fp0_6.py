fn = lambda: None
# Test fn.__code__.co_varnames
print(fn.__code__.co_varnames)
# Test fn.__code__.co_argcount
print(fn.__code__.co_argcount)

# __code__ is an attribute of the function object
print(type(fn.__code__))

# __code__ itself is an object that also has other attributes
print(dir(fn.__code__))

# Test fn.__code__.co_argcount
print(fn.__code__.co_argcount)

#print(fn.__code__.co_names)
#print(fn.__code__.co_consts)
#print(fn.__code__.co_varnames)
#print(fn.__code__.co_nlocals)
#print(fn.__code__.co_stacksize)
#print(fn.__code__.co_flags)
#print(fn.__code__.co_code)
#print(fn.__code__.co_lnotab)
#print(fn.__
