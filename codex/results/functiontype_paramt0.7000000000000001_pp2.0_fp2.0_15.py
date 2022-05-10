from types import FunctionType
list(FunctionType(add.__code__, globals())(1, 2))

# In[ ]:

from types import FunctionType
list(FunctionType(add.__code__, globals())(1, 2, 3))

# In[ ]:

from types import FunctionType
list(FunctionType(add.__code__, globals())(1))

# In[ ]:

from types import FunctionType
list(FunctionType(add.__code__, globals())(1, 2, 3, 4))

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:
