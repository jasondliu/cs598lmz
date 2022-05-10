from types import FunctionType
list(FunctionType(lambda x: x, {}, None, None, None).__code__.co_varnames)

# ['x']

# __code__.co_consts

# The tuple of constants used by the bytecode.

# In[ ]:


from types import FunctionType
list(FunctionType(lambda x: x, {}, None, None, None).__code__.co_consts)

# [<function <lambda> at 0x7f5c0d9d7c80>, None]

# __code__.co_names

# The tuple of names used by the bytecode.

# In[ ]:


from types import FunctionType
list(FunctionType(lambda x: x, {}, None, None, None).__code__.co_names)

# []

# __code__.co_nlocals

# The number of local variables used by the bytecode.

# In[ ]:


from types import FunctionType
FunctionType(lambda x: x, {}, None, None, None).__code__.co_nlocals
