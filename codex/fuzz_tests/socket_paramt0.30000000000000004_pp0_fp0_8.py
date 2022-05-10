import socket
socket.if_indextoname(1)

# In[ ]:


#get_ipython().system('pip install netifaces')
import netifaces
netifaces.interfaces()
netifaces.ifaddresses('lo')
netifaces.ifaddresses('eth0')
netifaces.ifaddresses('wlan0')

# In[ ]:


#get_ipython().system('pip install netaddr')
import netaddr
netaddr.IPNetwork('10.0.0.0/8')
netaddr.IPNetwork('10.0.0.0/8').size
netaddr.IPNetwork('10.0.0.0/8').cidr
netaddr.IPNetwork('10.0.0.0/8').netmask
netaddr.IPNetwork('10.0.0.0/8').broadcast
netaddr.IPNetwork('10.0.0.0/8').ip
netaddr.IPNetwork('10.0.0.0/8').network
netaddr.IPNetwork('10.0.0.0/8').hostmask
netaddr.IP
