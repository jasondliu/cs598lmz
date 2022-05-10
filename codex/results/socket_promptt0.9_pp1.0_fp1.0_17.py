import socket
# Test socket.if_indextoname() on 'wlan0'
socket.if_indextoname(3)

# In[ ]:

import pprint
with open('/proc/net/dev') as f:
    ifaces = f.readlines()
ifaces = [i.strip().split()[0][:-1] for i in ifaces[2:]]
pprint.pprint(ifaces)

# In[ ]:

import socket

# Test socket.if_indextoname() on 'wlan0'
socket.if_indextoname(3)

# ** Verificar interfaces LAN e WIFI

# In[ ]:

import socket     
import fcntl           
import struct         

def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                            ifname[:15]))[20:24])

