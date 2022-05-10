import socket
socket.if_indextoname(1)

import sys
import time

from scapy.all import *

# the public network interface
HOST = socket.if_indextoname(1)

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
s.bind((HOST, 0))

# we want to see the IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
print(s.recvfrom(65565))

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

# 1.1
# Sniffing with Scapy

# 1.2
# Sniffing with Scapy

# 1.3
# Sniffing with Scapy

#
