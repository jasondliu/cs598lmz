import socket
# Test socket.if_indextoname on a random additional index.

import random
import subprocess
import sys

from test.support import run_unittest, requires_linux_version
from test_socket import socket_helper

requires_linux_version(2, 6, 27)

class NetworkInterface(socket_helper.NetworkInterface):
    def __init__(self, name, index):
        super().__init__(name, index)
        self.name = name
        self.index = index
        self.flags = (
            self.IFF_UP |
            self.IFF_RUNNING |
            self.IFF_BROADCAST |
            self.IFF_MULTICAST
        )

        self.addresses = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.name)

    def get_ipv4_addresses(self):
        return [addr for addr in self.addresses
                if isinstance(addr, IPv4Address
