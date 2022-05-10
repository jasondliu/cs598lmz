import socket
socket.if_indextoname(14)

#!/usr/bin/env python
import os
import sys
import socket
import struct
import fcntl
import array

SIOCGIFCONF = 0x8912
BYTES = 4096

def get_all_interfaces():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', '\0' * BYTES)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        sock.fileno(),
        SIOCGIFCONF,
        struct.pack('iL', BYTES, names.buffer_info()[0])
    ))[0]
    namestr = names.tostring()
    return [namestr[i:i+32].split('\0', 1)[0] for i in range(0, outbytes, 32)]
</code>

