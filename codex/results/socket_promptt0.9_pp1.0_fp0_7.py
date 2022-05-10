import socket
# Test socket.if_indextoname() can take an integer.
p1 = socket.if_indextoname(1)

import socket
import os
import sys
import struct
import binascii
import traceback
import errno

RESOLV_CONF_PATH = "/etc/resolv.conf"
SIOCGIFHWADDR  = 0x8927
SIOCGIFADDR    = 0x8915

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            SIOCGIFADDR,
            struct.pack('256s', ifname[:15])
            )[20:24])
    except socket.error:
        return 1

def get_mac_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno
