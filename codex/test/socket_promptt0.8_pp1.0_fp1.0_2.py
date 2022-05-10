import socket
# Test socket.if_indextoname()

import _socket
import unittest
from test import support

interface_name = support.import_module('netifaces').gateways()['default'][
    socket.AF_INET][1]
if not interface_name:
    raise unittest.SkipTest("Couldn't get default interface name")

if not hasattr(_socket, 'if_indextoname'):
    raise unittest.SkipTest('if_indextoname not available')

# This should always return a valid interface name
interface_index = _socket.if_nametoindex(interface_name)
if interface_index < 0:
    raise unittest.SkipTest('Could not get the interface index')

if not hasattr(_socket, 'if_nameindex'):
    raise unittest.SkipTest('if_nameindex not available')

# Do this to test the two functions are compatible
nameindex_index, nameindex_name = next(iter(
    _socket.if_nameindex()))
if nameindex_name == 'lo':
    raise unittest.Skip
