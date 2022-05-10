import socket
socket.if_indextoname(2)

# In[ ]:


# Get the IP address of a given network interface
import socket
socket.if_nameindex()


# In[ ]:


# Get the name of a socket's service
import socket
socket.getservbyname('http')

# In[ ]:


# Get the port for a service
import socket
socket.getservbyport(80)

# In[ ]:


# Get the address info of a client
import socket
socket.getaddrinfo('www.python.org', 80)

# In[ ]:


# Get the canonical name of a host
import socket
socket.getfqdn('www.python.org')

# In[ ]:


# Get the host name of a socket
import socket
socket.gethostname()

# In[ ]:


# Get the host name of a socket
import socket
socket.gethostbyname('www.python.org')

# In[ ]:


# Get the host name of a socket
import socket
