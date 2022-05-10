import socket
# Test socket.if_indextoname() on Linux
from socket import if_indextoname, if_nameindex, if_nametoindex
from socket import SOME_INTERESTING_BYTE_ORDER, IF_NAMESIZE
from socket import IPPROTO_IP, IP_ADD_MEMBERSHIP


def _indextoname(index):
    """Assume index is valid, return the corresponding interface name."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = sock.getsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, IF_NAMESIZE)
    return (bytes[:IF_NAMESIZE]).decode('ascii')


class TestIfIndextoname:
    def test_error_conditions(self):
        self.assertRaises(OverflowError, if_indextoname, 2**32)
        self.assertRaises(OSError, if_indextoname, 0)

