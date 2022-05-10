import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

# In[1]:


print(fun())


# In[2]:


# create a type that can be used to describe the function.
# This function takes two integers, and returns an integer.
