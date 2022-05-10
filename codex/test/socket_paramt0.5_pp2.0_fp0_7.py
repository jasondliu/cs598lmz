import socket
socket.if_indextoname(3)

# In[ ]:


import socket
socket.if_indextoname(0)

# In[ ]:


import socket
socket.gethostbyname('www.google.com')

# In[ ]:


import socket
socket.gethostbyname_ex('www.google.com')

# In[ ]:


import socket
socket.gethostbyname_ex('www.google.com')[2]

# In[ ]:


import socket
socket.gethostname()

# In[ ]:


import socket
socket.gethostbyaddr('127.0.0.1')

# In[ ]:


import socket
socket.getservbyname('http')

# In[ ]:


import socket
socket.getservbyport(80)

# In[ ]:


import socket
socket.getprotobyname('tcp')

# In[ ]:


import socket
socket.getprotobyname('udp')

# In[ ]:


import socket
socket.get
