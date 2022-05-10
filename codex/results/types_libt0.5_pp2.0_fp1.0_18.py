import types
types.FunctionType


# In[13]:


class A:
    pass
isinstance(A, type)


# In[14]:


class A:
    pass
class B(A):
    pass
isinstance(B, A)


# In[15]:


class A:
    pass
class B(A):
    pass
isinstance(B(), A)


# In[16]:


class A:
    pass
class B(A):
    pass
isinstance(A(), A)


# In[17]:


class A:
    pass
class B(A):
    pass
isinstance(B(), B)


# In[18]:


class A:
    pass
class B(A):
    pass
isinstance(A(), B)


# In[19]:


class A:
    pass
class B(A):
    pass
isinstance(B, object)


# In[20]:


class A:
    pass
class B(A):
    pass
isinstance(B(), object)


# In[21
