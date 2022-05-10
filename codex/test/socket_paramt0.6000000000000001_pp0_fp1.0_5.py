import socket
socket.if_indextoname(9)

#%%

import os
import pprint
import socket
import struct

SIOCGIFADDR = 0x8915
SIOCGIFNETMASK = 0x891b
SIOCGIFBRDADDR = 0x8919

def get_ip(iface = 'eth0'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        sock.fileno(),
        SIOCGIFADDR,
        struct.pack('256s', iface[:15])
    )[20:24])

def get_netmask(iface = 'eth0'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        sock.fileno(),
        SIOCGIFNETMASK,
        struct.pack('256s', iface[:15])
    )[20:24])


