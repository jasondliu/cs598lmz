from types import FunctionType
list(FunctionType(f.__code__, {}, name="g"))


# In[20]:


g = FunctionType(f.__code__, {}, name="g")
g(1, 2)


# In[21]:


import types
type(g.__closure__[0].cell_contents)


# In[22]:


h = lambda x, y, z=1: x + y + z
h(1, 2)


# In[23]:


g.__code__.co_freevars


# In[24]:


g.__closure__[0]


# In[25]:


g.__closure__[0].cell_contents


# In[27]:


from types import CodeType
co = CodeType(
    h.__code__.co_argcount,
    h.__code__.co_kwonlyargcount,
    h.__code__.co_nlocals,
    h.__code__.co_stacksize,
    h.__code__.co_flags,
    h.__
