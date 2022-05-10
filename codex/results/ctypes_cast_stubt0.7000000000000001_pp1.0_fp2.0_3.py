import ctypes
ctypes.cast(a, ctypes.py_object).value

#https://stackoverflow.com/questions/298855/how-to-determine-the-type-of-an-array-in-numpy
print(a.dtype, a.shape)


# In[2]:


a= np.array([(1,2,3),(4,5,6)])

b= np.array([(1,2,3),(4,5,6)])
c= np.array([(1,2,3),(4,5,6)])


# In[3]:


a


# In[4]:


a.ndim


# In[5]:


a.size


# In[6]:


a.dtype


# In[7]:


a.shape


# In[8]:


#use of reshape

a.reshape(3,2)


# In[9]:


a.reshape(6,1)


# In[10]:


a.reshape(1
