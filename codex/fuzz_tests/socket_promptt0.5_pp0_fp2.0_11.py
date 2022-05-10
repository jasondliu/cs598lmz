import socket
# Test socket.if_indextoname()

#if_indextoname(index)

#Return the interface name for a given numeric index.

#The numeric index should have been retrieved from the SIOCGIFINDEX ioctl.

#Availability: Unix.

import socket
import fcntl
import struct

def get_interface_name(ifindex):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.if_indextoname(ifindex)

print get_interface_name(2)
