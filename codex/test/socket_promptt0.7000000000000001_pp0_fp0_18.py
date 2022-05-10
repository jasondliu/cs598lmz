import socket
# Test socket.if_indextoname for Python 3.4+ only.
try:
    socket.if_indextoname(1)
except AttributeError:
    pass
else:
    def _get_interface_mac(ifname):
        """Returns the MAC address of an interface."""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s',
                          ifname[:15]))
        s.close()
        return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

