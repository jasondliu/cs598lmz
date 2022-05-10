import socket
socket.if_indextoname(2)

# In[ ]:


#!pip install netifaces
import netifaces
netifaces.interfaces()
netifaces.ifaddresses('en0')
netifaces.ifaddresses('en0')[netifaces.AF_LINK]
netifaces.ifaddresses('en0')[netifaces.AF_LINK][0]['addr']
netifaces.ifaddresses('en0')[netifaces.AF_INET]
netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
netifaces.ifaddresses('en0')[netifaces.AF_INET6]
netifaces.ifaddresses('en0')[netifaces.AF_INET6][0]['addr']

# In[ ]:


#!pip install netaddr
import netaddr
netaddr.IPAddress('192.168.1.1')
netaddr.IPNetwork('192.168.1.0/24')
netaddr.IPNetwork('192.168
