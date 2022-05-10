import socket
socket.if_indextoname(socket.if_nametoindex(iface))
</code>
or
<code>import fcntl
fcntl.ioctl(sock.fileno(), SIOCGIFNAME, interface)
</code>
but I don't know how to convert a MAC address into an interface.


A:

You can do this with <code>ioctl</code> again:
<code>import socket
import fcntl
import struct

def get_mac_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])
</code>

