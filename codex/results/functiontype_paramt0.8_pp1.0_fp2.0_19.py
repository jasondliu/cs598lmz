from types import FunctionType
list(FunctionType(fib,globals(),'fib').__globals__.keys())


# In[27]:


fib.__code__


# In[28]:


fib.__code__.co_varnames


# In[29]:


fib.__code__.co_argcount
