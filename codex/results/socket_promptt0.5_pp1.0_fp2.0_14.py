import socket
# Test socket.if_indextoname()
#
# This test is intended to be run on a machine with two or more network
# interfaces.  The first interface is assumed to be the loopback interface
# and the second interface is assumed to be the first non-loopback interface.
#
# The test attempts to convert the interface index of the loopback interface
# to a name and then the interface index of the first non-loopback interface
# to a name.  The test passes if the names are correctly returned.

import unittest
import socket
import sys

class If_indextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # Get the interface index of the loopback interface.
        loopback_if_index = socket.if_nametoindex('lo')
        # Get the interface index of the first non-loopback interface.
        if_index = socket.if_nametoindex('eth0')
        # Convert the interface index of the loopback interface to a name.
        if_name = socket.if_indextoname(loopback_if_index)
       
