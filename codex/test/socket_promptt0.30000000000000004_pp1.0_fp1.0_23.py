import socket
# Test socket.if_indextoname

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not available")

class IfIndexToNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # get the interface index of the loopback interface
        lo_index = socket.if_nametoindex('lo')
        # get the interface name of the loopback interface
        lo_name = socket.if_indextoname(lo_index)
        # check that the name is the loopback interface
        self.assertEqual(lo_name, 'lo')

    def test_if_indextoname_invalid(self):
        # get the interface name of an invalid interface index
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
