import socket
socket.if_indextoname(3)

# In[ ]:


#getifaddrs()
import socket
socket.getifaddrs()

# In[ ]:


#getnameinfo()
import socket
socket.getnameinfo(('127.0.0.1', 80), 0)

# In[ ]:


#getprotobyname()
import socket
socket.getprotobyname('tcp')

# In[ ]:


#getservbyname()
import socket
socket.getservbyname('http', 'tcp')

# In[ ]:


#getservbyport()
import socket
socket.getservbyport(80, 'tcp')

# In[ ]:


#gethostbyname()
import socket
socket.gethostbyname('www.google.com')

# In[ ]:


#gethostbyname_ex()
import socket
socket.gethostbyname_ex('www.google.com')

# In[ ]:


#gethostbyaddr()
import socket
socket.gethostbyaddr('216
