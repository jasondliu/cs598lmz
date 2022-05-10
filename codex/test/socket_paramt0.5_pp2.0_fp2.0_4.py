import socket
socket.if_indextoname(3)

import fcntl
fcntl.ioctl(sock.fileno(),0x8915,struct.pack('256s',ifname[:15]))[20:24]

import struct
import socket
import fcntl
ifname = 'lo'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
