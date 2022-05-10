import socket
# Test socket.if_indextoname()
a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print socket.gethostname()
print socket.gethostbyaddr("127.0.0.1")
for x in range(3, 4):
    print x, ":", socket.if_indextoname(x)
"""
"""
import socket
import sys
import struct
import time

MULTI_GROUP_IP = '224.0.0.1'
MULTI_GROUP_MASK = '224.0.0.0'

INADDR_ANY = '0.0.0.0'

#int32_mask = struct.unpack('@I', socket.inet_aton('255.255.255.255')
#int32_mask[0]

def gen_netmask_int32(prefix):
    global int32_mask
    mask = 0;
    for x in range(prefix):
        mask = (mask << 1) + 1
    mask = mask << (32 - prefix)
    return mask

def gen_net
