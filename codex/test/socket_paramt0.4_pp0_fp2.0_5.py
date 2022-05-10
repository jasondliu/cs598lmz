import socket
socket.if_indextoname(3)

#%%
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

#%%
get_ip_address('eth0')

#%%
get_ip_address('wlan0')

#%%
import os
import socket
import fcntl
import struct
import array

SIOCGIFCONF = 0x8912 #define SIOCGIFCONF
BYTES = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
names = array.array('B', '\0' * BYTES)
