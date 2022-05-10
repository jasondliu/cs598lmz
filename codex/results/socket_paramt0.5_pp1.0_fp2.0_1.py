import socket
socket.if_indextoname(3)

# Get the IP address of an interface
socket.if_nameindex()
socket.if_nameindex()[3][1]

# Get the MAC address of an interface
import fcntl, socket, struct
def get_mac_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]
get_mac_address('eth0')

# Get the MAC address of the system
import uuid
uuid.getnode()

# Get the IP address of the host
import socket
socket.gethostbyname(socket.gethostname())
socket.gethostbyname_ex(socket.gethostname())

# Get the internal IP address of the host
# (or the IP address of the interface
# facing the specified
