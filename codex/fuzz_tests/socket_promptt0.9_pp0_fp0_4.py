import socket
# Test socket.if_indextoname()
"""
>>> import socket
>>> socket.AF_INET
2
>>> socket.PF_INET
2
>>> socket.SOCK_STREAM
1
>>> socket.SOCK_DGRAM
2
>>> socket.AF_IPX
4
>>> socket.PF_IPX
4
>>> socket.SOCK_RAW
3
>>> socket.AF_NETLINK
16
>>> socket.PF_NETLINK
16
>>> socket.SOCK_SEQPACKET
5
>>> socket.AF_UNIX
1
>>> socket.PF_UNIX
1
>>> socket.AF_INET6
10
>>> socket.PF_INET6
10
>>> socket.SOCK_PACKET
10
>>> socket.AF_BLUETOOTH
31
>>> socket.PF_BLUETOOTH
31
>>>
"""

import os
import struct
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
s.bind(("127.0.0.1", 0))
s
