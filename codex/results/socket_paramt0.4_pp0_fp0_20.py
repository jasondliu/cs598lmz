import socket
socket.if_indextoname(3)

#get the IP address of an interface
socket.if_nameindex()
socket.if_nameindex()[3][1]

#get the MAC address of an interface
import fcntl
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
mac = ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

#get the IP address of an interface
import socket
import struct
import fcntl

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20
