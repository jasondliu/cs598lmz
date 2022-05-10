import socket
socket.if_indextoname(1)

# Check for configured interfaces
from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6

