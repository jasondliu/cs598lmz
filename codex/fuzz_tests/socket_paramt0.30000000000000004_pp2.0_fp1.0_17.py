import socket
socket.if_indextoname(1)

# get the IP address of the interface
socket.if_nameindex()
socket.if_nameindex()[1][1]

# get the MAC address of the interface
import uuid
uuid.getnode()

# get the IP address of the interface
import fcntl
import struct
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

get_ip_address('eth0')
