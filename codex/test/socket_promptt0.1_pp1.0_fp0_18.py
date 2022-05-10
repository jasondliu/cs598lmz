import socket
# Test socket.if_indextoname()

import unittest
import socket
import os
import sys
import errno
import platform
import subprocess

from test import support
from test.support import import_module

# Skip test if there is no interface on this machine
has_any_ip_address = False
for info in socket.getaddrinfo(None, 0, socket.AF_UNSPEC,
                               socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = info
    if af == socket.AF_INET or af == socket.AF_INET6:
        has_any_ip_address = True
        break

@unittest.skipUnless(has_any_ip_address, 'requires an IP address')
class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        # Get all interface indices
        if_indices = socket.if_indices()
        # Try to get the name of each interface

