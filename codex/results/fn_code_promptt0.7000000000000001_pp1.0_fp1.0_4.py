fn = lambda: None
# Test fn.__code__.co_args to determine if there were any arguments
# in the function definition.
#print(fn.__code__.co_args)

#print(fn.__code__.co_argcount)


#print(fn.__code__.co_varnames)

#print(fn.__code__.co_nlocals)

#print(fn.__code__.co_names)

#print(fn.__code__.co_consts)

#print(fn.__code__.co_freevars)

#print(fn.__code__.co_cellvars)

#print(fn.__code__.co_stacksize)

#print(fn.__code__.co_flags)

#print(fn.__code__.co_firstlineno)

#print(fn.__code__.co_lnotab)


# In[23]:


# Define a function that takes in a list of numbers and returns a string.
def to_string(nums):
    return ''.join(
