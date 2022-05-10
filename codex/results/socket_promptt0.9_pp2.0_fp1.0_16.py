import socket
# Test socket.if_indextoname() function

import unittest
from test import test_support

interface_name = 'lo'
interface_indices = filter(bool, socket.if_indices.values())

# The test_support.find_unused_port() utility relies on the bind()
# method. However, bind() can fail with a socket.error unless the
# socket has been bound to a device using SO_BINDTODEVICE. For this
# reason, it is necessary to find an interface index that exists on
# the testing machine (using the interface_indices variable). But
# SO_BINDTODEVICE does not work on the loopback, so we choose the
# last available device that is not the loopback.
if interface_name == 'lo':
    for index in interface_indices:
        if socket.if_indextoname(index) != 'lo':
            interface_name = socket.if_indextoname(index)
            break

class NetworkInterfaceTests(unittest.TestCase):
    def test_if_name(self):
        for index in interface_ind
