import socket
socket.if_indextoname(3)

# In[ ]:


import socket
socket.if_nametoindex('lo')

# In[ ]:


import socket
socket.gethostbyname('www.google.com')

# In[ ]:


import socket
socket.gethostbyname_ex('www.google.com')

# In[ ]:


import socket
socket.gethostbyaddr('172.217.4.174')

# In[ ]:


import socket
socket.gethostbyname_ex('www.google.com')

# In[ ]:


import socket
socket.gethostname()

# In[ ]:


import socket
socket.gethostbyname_ex(socket.gethostname())

# In[ ]:


import socket
socket.gethostbyname_ex(socket.gethostname())[2]

# In[ ]:


import socket
socket.gethostbyname_ex(socket.gethostname())[2][0]

# In[ ]:


import socket
socket.gethostbyname
