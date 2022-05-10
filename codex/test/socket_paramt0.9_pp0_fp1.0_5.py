import socket
socket.if_indextoname(1)

import struct
struct.unpack('9s',b'\x01\xa0\xc2')

import fcntl

fcntl.ioctl(fd,name,request,arg)

