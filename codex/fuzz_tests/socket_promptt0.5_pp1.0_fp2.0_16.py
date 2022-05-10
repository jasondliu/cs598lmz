import socket
# Test socket.if_indextoname()
import sys
import unittest
from test import support
from test.support import import_module, run_unittest

# Skip test if IPv6 is not supported
import_module('socket')
has_ipv6 = socket.has_ipv6
if not has_ipv6:
    raise unittest.SkipTest("IPv6 is not supported on this platform")

import_module('select')

# Skip test if the interface configuration is not sane enough
if not hasattr(socket, 'if_nameindex'):
    raise unittest.SkipTest("if_nameindex() not available on this platform")

# Skip test if there is no loopback interface
name_indices = socket.if_nameindex()
has_lo = False
for (index, name) in name_indices:
    if name == 'lo':
        has_lo = True
        break
if not has_lo:
    raise unittest.SkipTest("No loopback interface available")

# Skip test if the loopback interface has no IPv6 addresses
if not hasattr(socket,
