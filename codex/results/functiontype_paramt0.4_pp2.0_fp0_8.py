from types import FunctionType
list(FunctionType(lambda: None, globals()).__code__.co_varnames)

# In[ ]:


def get_var_names(func):
    return list(FunctionType(func, globals()).__code__.co_varnames)


# In[ ]:


get_var_names(lambda: None)


# In[ ]:


get_var_names(lambda x: None)


# In[ ]:


get_var_names(lambda x, y: None)


# In[ ]:


get_var_names(lambda x, y, z: None)


# In[ ]:


get_var_names(lambda x, y=1: None)


# In[ ]:


get_var_names(lambda x, y=1, z=2: None)


# In[ ]:


get_var_names(lambda x, y=1, z=2, *args: None)


# In[ ]:


get_var_names(lambda x, y=1, z=2, *
