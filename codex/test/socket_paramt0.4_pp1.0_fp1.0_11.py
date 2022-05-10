import socket
socket.if_indextoname(3)

# In[ ]:


import socket
socket.if_nameindex()

# In[ ]:


import socket
socket.if_nametoindex('lo')

# In[ ]:


import socket
socket.getaddrinfo('www.google.com', 80)

# In[ ]:


import socket
socket.getaddrinfo('127.0.0.1', 80)

# In[ ]:


import socket
socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM)

# In[ ]:


import socket
socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# In[ ]:


import socket
socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_CANONNAME)

#
