import ctypes
ctypes.cast(None, ctypes.py_object).value


# In[39]:


import ctypes
ctypes.cast(ctypes.py_object(None), ctypes.c_void_p).value


# In[40]:


import ctypes
ctypes.cast(ctypes.py_object(256), ctypes.c_void_p).value


# In[41]:


import ctypes
ctypes.cast(ctypes.py_object([1, 2, 3]), ctypes.c_void_p).value


# In[42]:


import ctypes
ctypes.cast(ctypes.py_object(1.23), ctypes.c_void_p).value


# In[43]:


import ctypes
ctypes.cast(ctypes.py_object(b'abcd'), ctypes.c_void_p).value


# In[44]:


import ctypes
ctypes.cast(ctypes.py_object('abcd'), ctypes.c_void_p).value


# In[45]:


import ctypes

