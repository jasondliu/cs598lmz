import socket
socket.if_indextoname(1)

# In[ ]:


# Get the IP address of an interface
import socket
socket.if_nameindex()

# In[ ]:


# Get the name of a service for a given protocol and port number
import socket
socket.getservbyport(80, 'tcp')

# In[ ]:


# Get the port number for a given service name and protocol
import socket
socket.getservbyname('http', 'tcp')

# In[ ]:


# Get the hostname of the machine
import socket
socket.gethostname()

# In[ ]:


# Get the fully qualified hostname
import socket
socket.getfqdn()

# In[ ]:


# Get the IP address of a host
import socket
socket.gethostbyname('www.python.org')

# In[ ]:


# Get all of the IP addresses associated with a name
import socket
socket.gethostbyname_ex('www.python.org')

# In[ ]:


# Get the canonical name of a host
import socket
