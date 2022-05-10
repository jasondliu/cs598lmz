import socket
socket.if_indextoname(2)
# 'en0'
socket.if_indextoname(11)
# 'en1'

# Network Interface Lookup Functions

import socket
socket.if_nameindex()
# [(1, 'lo0'), (2, 'en0'), (3, 'p2p0'), (4, 'awdl0'), (5, 'utun0'), (6, 'utun1'), (7, 'utun2')]
socket.if_nameindex()[0][1]
# 'lo0'

# Iterating over Network Interfaces

import netifaces
netifaces.interfaces()
# ['awdl0', 'en0', 'lo0', 'p2p0', 'utun0', 'utun1', 'utun2']
netifaces.interfaces()[0]
# 'awdl0'
netifaces.ifaddresses(netifaces.interfaces()[0])
# {18: [{'broadcast': 'ff:ff:ff:ff:ff:ff', 'addr': '02:01:02:03:
