import socket
socket.if_indextoname(3)

# In[ ]:


# get the name of the interface associated with a given index
import socket
socket.if_nameindex()

# In[ ]:


# get the MAC address of a network interface
import netifaces as ni
ni.ifaddresses('eth0')
ni.ifaddresses('eth0')[ni.AF_LINK][0]['addr']

# In[ ]:


# get the IP address of a network interface
import netifaces as ni
ni.ifaddresses('eth0')
ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

# In[ ]:


# get the broadcast address of a network interface
import netifaces as ni
ni.ifaddresses('eth0')
ni.ifaddresses('eth0')[ni.AF_INET][0]['broadcast']

# In[ ]:


# get the netmask of a network interface
import netifaces as ni
ni.ifaddresses('eth0')
ni.ifaddresses('eth0')[
