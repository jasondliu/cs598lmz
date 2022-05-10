import socket
# Test socket.if_indextoname()
try:
    socket.if_nametoindex('lo')
except AttributeError:
    raise unittest.SkipTest("if_nametoindex not defined")

from vpp_interface import VppInterface
from vpp_ip_route import VppIpRoute, VppRoutePath

from scapy.layers.l2 import Ether
from scapy.layers.inet6 import IPv6, UDP, TCP
from scapy.packet import Raw
from util import ppp


class TestIP6Neighbor(VppTestCase):
    """IPv6 Neighbor Test Case"""

    @classmethod
    def setUpClass(cls):
        super(TestIP6Neighbor, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestIP6Neighbor, cls).tearDownClass()

