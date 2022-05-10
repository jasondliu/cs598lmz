import socket
socket.if_indextoname('3')
socket.gethostbyname('192.168.43.9')


# In[16]:


socket.getaddrinfo('www.cs.princeton.edu',80)


# # Bytes, Strings, and Character Encodings

# In[17]:


blist = [1,2,3,255]
the_bytes = bytes(blist)
the_bytes


# In[18]:


the_bytes[1] 


# In[19]:


the_byte_array = bytearray(blist)
the_byte_array


# In[20]:


a=255
bin(a)


# In[21]:


a=0b11111111
a


# In[22]:


a=0xff
a


# In[23]:


bytes([0b11110000, 0b10101010])


# In[24]:


the_bytes[0]


# In[25]:


the_bytes[0]=0b11110000


# In[26]:


the
