import socket
socket.if_indextoname(2)

# In[7]:


# if_indextoname(2)

# In[8]:


socket.if_nameindex()

# In[9]:


socket.gethostname()

# In[10]:


socket.gethostbyname('www.python.org')

# In[11]:


socket.gethostbyname_ex('www.python.org')

# In[12]:


socket.gethostbyaddr('216.58.192.78')

# In[13]:


socket.getnameinfo(('216.58.192.78', 80), 0)

# In[14]:


# socket.getnameinfo(('216.58.192.78', 80), 0)

# In[15]:


socket.getprotobyname('tcp')

# In[16]:


socket.getservbyname('http', 'tcp')

# In[17]:


socket.getservbyport(80, 'tcp')

# In[18]:


# socket.
