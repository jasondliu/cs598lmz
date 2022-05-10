import socket
# Test socket.if_indextoname, socket.if_indextoname.

# This is a test for if_indextoname() and if_indextoname().
# Both functions accept an interface index, and return the corresponding
# interface name and interface index respectively.
# Currently only the interface name is tested.

import socket
import unittest
from test import support

class InterfaceTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Get the interface index of 'lo'
        lo = socket.if_nametoindex('lo')
        # Get the interface name of the loopback interface
        name = socket.if_indextoname(lo)
        # Compare the interface index of the name with the one we got earlier
        self.assertEqual('lo', name)

