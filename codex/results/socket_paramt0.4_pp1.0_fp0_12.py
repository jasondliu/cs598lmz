import socket
socket.if_indextoname(3)

# get the name of the interface
socket.gethostname()

# get the IP address of the interface
socket.gethostbyname(socket.gethostname())

# get the MAC address of the interface
import uuid
uuid.getnode()

# get the MAC address of the interface
import netifaces
netifaces.ifaddresses('enp0s3')[netifaces.AF_LINK][0]['addr']

# get the MAC address of the interface
import fcntl
import struct
def get_mac(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])
get_mac('enp0s3')
