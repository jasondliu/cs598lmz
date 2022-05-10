import socket
# Test socket.if_indextoname()
#
# This test verifies that socket.if_indextoname() returns the correct
# interface name for a given interface index
#
# It is assumed that the current machine has at least two network interfaces
# installed
#
# This test is known to fail on Windows, as Windows does not support
# socket.if_indextoname().

import socket
import sys
import unittest
from test import support

@unittest.skipUnless(hasattr(socket, 'if_indextoname'),
                     'socket.if_indextoname required')
class IfIndexToNameTest(unittest.TestCase):
    def testIfIndexToName(self):
        # Obtain the names of all interfaces on the current machine
        interfaces = socket.if_nameindex()
        # Obtain a list of interface tuples (index, name)
        if_list = [(index, socket.if_indextoname(index)) for index, name in interfaces]
        # Verify that the interface names match the expected values
        for index, name in if_list:
            self.assert
