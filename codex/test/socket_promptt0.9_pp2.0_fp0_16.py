import socket
# Test socket.if_indextoname()

from test import support
from test.test_ipaddress import cidr_to_int, cidr_to_prefixlen, is_cidr
from test.support import bigaddr_available

# This just tests when the interface name is not found or an index is
# out of range.
class IfIndexTest(unittest.TestCase):
    def setUp(self):
        self.defaultif = socket.if_indextoname(cidr_to_int('192.0.2.0/24'))
        if self.defaultif is None:
            self.defaultip = None
        else:
            self.defaultip = cidr_to_int(socket.if_nameindex()[self.defaultif])

    def test_if_indextoname_unknown(self):
        hostisolated = False
        index = socket.if_nametoindex('lo')
        if_index = cidr_to_int('192.255.255.255/24')
        if if_index == 2**32-1:
            raise self
