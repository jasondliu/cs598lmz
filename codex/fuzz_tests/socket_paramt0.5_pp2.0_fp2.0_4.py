import socket
socket.if_indextoname(3)

import fcntl
fcntl.ioctl(sock.fileno(),0x8915,struct.pack('256s',ifname[:15]))[20:24]

import struct
import socket
import fcntl
ifname = 'lo'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
return fcntl.ioctl(sock.fileno(),0x8915,struct.pack('256s',ifname[:15]))[20:24]

import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

import socket
import fcntl
import struct
