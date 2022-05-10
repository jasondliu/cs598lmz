import socket
# Test socket.if_indextoname() support
try:
    socket.if_indextoname(1)
except AttributeError:
    socket.if_indextoname = None
def interface_enabled(ifname):
    """
    Take interface name and return True if it is enabled.

    @param ifname: Name of the interface in form of a string.
    @return: True if interface is enabled, False otherwise.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ifindex = socket.if_nametoindex(ifname)
        if socket.if_indextoname(ifindex) == ifname:
            SIOCGIFFLAGS = 0x8913
            ifreq = struct.pack('16si', ifname, 0)
            res = fcntl.ioctl(sock.fileno(), SIOCGIFFLAGS, ifreq)
            _, flags = struct.unpack('16si', res)
            return bool(flags & 1)
        else:
            return False
    finally:
       
