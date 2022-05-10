import socket
socket.if_indextoname(16)

try:
    import netifaces
except ImportError:
    netifaces = None

from twisted.trial import unittest
from twisted.internet import defer
from ooni import errors as e
from ooni.utils.net import (isPrivateIP, isIPAddress, isIPv8Address,
                            getMajorIPBlock, getLocalIPv6, getLocalIP)
from ooni.utils import log

log.start()


class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.expected_ips = {
            "192.168.1.233": True,
            "192.168.2.31": True,
            "127.0.0.1": False,
            "8.8.8.8": False,
            "192.168.1.0": True,
            "10.10.10.10": True,
            "127.1.1.1": False
        }
        self.expected_ipv6s = {
            "fd00:0:0:0:0:
