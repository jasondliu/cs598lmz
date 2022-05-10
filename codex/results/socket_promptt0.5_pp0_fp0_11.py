import socket
# Test socket.if_indextoname()

SOCKET_TEST_IFACE = "lo"

def _if_nametoindex(ifname):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        ifr = struct.pack('16sh', ifname, 0)
        try:
            res = fcntl.ioctl(s.fileno(), SIOCGIFINDEX, ifr)
        except IOError as e:
            if e.errno == errno.EINVAL:
                raise ValueError('invalid interface name')
            raise
        return struct.unpack('16sh', res)[1]

def _if_indextoname(ifindex):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        ifr = struct.pack('16si', b'', ifindex)
        try:
            res = fcntl.ioctl(s.fileno(), SIOCGIFNAME, ifr)
        except IOError as e:
            if e
