import socket
socket.if_indextoname(3)

bcast_ip = socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8919,  # SIOCGIFBRDADDR
    struct.pack('256s', ifname[:15])
)[20:24])

print bcast_ip

import socket
import struct
import fcntl

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ifname = 'wlan0'
ifname2 = 'eth0'
ifname3 = 'lo'

#get ip address
ip = socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8915,  # SIOCGIFADDR
    struct.pack('256s', ifname[:15])
)[20:24])

print ip

#get network mask
netmask = socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x891b,  # SIOCGIFNET
