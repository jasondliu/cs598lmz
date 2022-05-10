import socket
socket.if_indextoname(3)

# In[ ]:


socket.gethostname()


# In[ ]:


socket.gethostbyname(socket.gethostname())


# In[ ]:


socket.gethostbyname('www.google.com')


# In[ ]:


socket.gethostbyname_ex('www.google.com')


# In[ ]:


socket.gethostbyaddr('216.58.197.68')


# In[ ]:


socket.getaddrinfo('www.google.com', 80)


# In[ ]:


socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM)


# In[ ]:


socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_DGRAM)


# In[ ]:


socket.getaddrinfo('www.google.com', 80, socket.AF_INET6, socket.SOCK_STREAM)


# In[ ]:
