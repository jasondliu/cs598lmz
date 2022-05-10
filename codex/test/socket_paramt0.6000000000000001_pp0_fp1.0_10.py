import socket
socket.if_indextoname(4)

# In[ ]:


# Get the IP address of the interface
socket.if_nameindex()


# In[ ]:


# Get the MAC address of the interface
import uuid
uuid.getnode()


# In[ ]:


# Get the IPv4 address
import socket
socket.gethostbyname(socket.getfqdn())


# In[ ]:


# Get the IPv6 address
import socket
socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6, 0, socket.SOL_TCP)


# In[ ]:


# Get the MAC address of the interface
import netifaces as ni
ni.ifaddresses('eth0')[ni.AF_LINK][0]['addr']


# In[ ]:


# Get the IPv4 address
import netifaces as ni
ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']


# In[ ]:


# Get the IPv6 address
import netifaces as ni
ni
