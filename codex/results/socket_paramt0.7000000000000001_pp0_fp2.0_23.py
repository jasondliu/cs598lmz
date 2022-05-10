import socket
socket.if_indextoname(0x4)

# In[6]:

import uuid
get_ipython().system(u'hostname')
get_ipython().system(u'hostname -I')

prefix_48 = uuid.getnode() >> 16

# In[7]:

socket.if_indextoname(0x5)

# In[8]:

import socket
import struct
import fcntl

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

get_ip_address('eth0')


# In[9]:

get_ipython().system(u'ifconfig')


# In[10]:

get_ipython().system(u'ifconfig eth0')



