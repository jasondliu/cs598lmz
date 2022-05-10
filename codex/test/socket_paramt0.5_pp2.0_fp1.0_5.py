import socket
socket.if_indextoname('1')

# In[ ]:


import socket
socket.if_nametoindex('lo')


# In[ ]:


import socket
socket.getaddrinfo('www.python.org',80)


# In[ ]:


import socket
socket.getaddrinfo('www.python.org',80,0,0,socket.IPPROTO_TCP)


# In[ ]:


import socket
socket.getaddrinfo('www.python.org',None)


# In[ ]:


import socket
socket.getaddrinfo('127.0.0.1',80,socket.AF_INET,socket.SOCK_STREAM)


# In[ ]:


import socket
socket.getaddrinfo('127.0.0.1',80,socket.AF_INET,socket.SOCK_STREAM,0,socket.AI_PASSIVE)


# In[ ]:


import socket
