fn = lambda: None
# Test fn.__code__
print(fn.__code__)
# Test fn.__code__.co_code
print(fn.__code__.co_code)

# Test fn.__code__.co_varnames
# Test fn.__code__.co_argcount
# Test fn.__code__.co_nlocals

def fn(a, b):
    c = a + b
    return c

print(fn.__code__.co_varnames)
print(fn.__code__.co_argcount)
print(fn.__code__.co_nlocals)

# Test fn.__code__.co_consts
# Test fn.__code__.co_names
# Test fn.__code__.co_filename
# Test fn.__code__.co_name
# Test fn.__code__.co_firstlineno
# Test fn.__code__.co_lnotab
# Test fn.__code__.co_freevars
# Test fn.__code__.co_cellvars


# In[ ]:


