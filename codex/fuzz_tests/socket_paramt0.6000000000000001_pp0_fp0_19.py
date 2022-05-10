import socket
socket.if_indextoname(5)

import psutil

net_io = psutil.net_io_counters(pernic=True)['en0']
print net_io.bytes_sent
print net_io.bytes_recv

import socket
import binascii
import struct

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))

print int2ip(ip2int('192.168.1.1'))

ip = '192.168.1.1'
print '.'.join(map(str, map(lambda x: int(x, 16), ip.split('.'))))

import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),

