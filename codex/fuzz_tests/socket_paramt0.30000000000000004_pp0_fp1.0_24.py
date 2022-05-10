import socket
socket.if_indextoname(3)

# get the MAC address of an interface
import uuid
print uuid.getnode()

# get the MAC address of an interface
import fcntl
import struct
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

# get the MAC address of an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# get the MAC address of an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# get the MAC address of an interface
import netifaces
netifaces.ifaddresses('eth0')[
