from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_code, a.gi_frame.f_globals)


# In[16]:


b.__name__


# In[17]:


b.__closure__


# In[18]:


b.__code__.co_freevars


# In[19]:


b.__code__.co_consts
