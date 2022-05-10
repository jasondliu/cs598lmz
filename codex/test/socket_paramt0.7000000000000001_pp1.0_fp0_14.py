import socket
socket.if_indextoname(1)
socket.if_indextoname(2)
socket.if_indextoname(3)
socket.if_indextoname(4)
socket.if_indextoname(5)

# Using scapy
from scapy.all import *

# Try this
conf.route.resync()
netifaces.interfaces()
socket.if_indextoname(1)
socket.if_indextoname(2)
socket.if_indextoname(3)
socket.if_indextoname(4)
socket.if_indextoname(5)
