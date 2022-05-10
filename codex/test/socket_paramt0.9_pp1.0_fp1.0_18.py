import socket
socket.if_indextoname(socket.if_nametoindex("eth0"))

import netifaces as ni
ni.ifaddresses('eth0')
ni.interfaces()
sep = "-" * 70

# This function just prints out basic information about
# each interface.
