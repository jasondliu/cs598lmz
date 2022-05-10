import socket
socket.if_indextoname(2)

# In[ ]:


# Get the MAC address of a network interface
import netifaces
netifaces.ifaddresses('eth0')

# In[ ]:


# Get the MAC address of a network interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK]

# In[ ]:


# Get the MAC address of a network interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# In[ ]:


# Get the IP address of a network interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# In[ ]:


# Get the IP address of a network interface
import netifaces
netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']

# In[ ]:


# Get the IP address of a network interface
import netif
