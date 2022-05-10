from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# In[ ]:


def get_vars_of(func):
    return list(FunctionType(func, {}).__code__.co_varnames)


# In[ ]:


get_vars_of(lambda: None)


# In[ ]:


def get_vars_of(func):
    return list(FunctionType(func, {}).__code__.co_varnames)


# In[ ]:


get_vars_of(lambda: None)


# In[ ]:


get_vars_of(lambda x: None)


# In[ ]:


get_vars_of(lambda x, y: None)


# In[ ]:


def add(x, y):
    return x + y

get_vars_of(add)


# In[ ]:


get_vars_of(add)


# In[ ]:


def get_vars_of(func):
    return
