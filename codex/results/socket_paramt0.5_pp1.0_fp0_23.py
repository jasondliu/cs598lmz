import socket
socket.if_indextoname(1)

# get the mac address of the interface
import uuid
print(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1]))

# get the mac address of the interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# get the mac address of the interface
import fcntl
import struct
def get_mac_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

get_mac_address('eth0')


# get the mac address of the interface
import netifaces
netifaces
