import socket
socket.if_indextoname(2)

import re
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


import os
import sys

# check if root
if not 'SUDO_UID' in os.environ.keys():
    print "Please run me as root"
    sys.exit(0)

uid = int(os.environ['SUDO_UID'])
gid = int(os.environ['SUDO_GID'])

# print get_ip_address('wlan0')

os.environ['XAUTHORITY'] = os.path.expanduser('~/.Xauthority')
os.environ['DISPLAY'] = ':1'

import os.path
import time

