import socket
# Test socket.if_indextoname, socket.if_nameindex, socket.if_nametoindex

# XXX: These tests assume that there is at least one interface
# configured on the machine.

# XXX: These tests assume that there are no more than 255 interfaces
# configured on the machine.

import unittest
import os
import sys
import socket
import array

# Skip test if IPv6 is not supported
if not hasattr(socket, "AF_INET6"):
    raise unittest.SkipTest("IPv6 is not supported")

# Skip test if IPv6 sockets don't support interface names
if sys.platform in ('linux', 'darwin') and not hasattr(socket, "IPV6_RECVPKTINFO"):
    raise unittest.SkipTest("IPv6 sockets don't support interface names")

