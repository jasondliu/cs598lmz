import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import test_support

ifname = test_support.find_unused_port(socket.AF_INET)

class IfIndexToNameTest(unittest.TestCase):
    def setUp(self):
        try:
            ifname
        except NameError:
            self.skipTest("requires ifname")
        self.ifname = ifname

    def testIfIndexToName(self):
        ifindex = socket.if_nametoindex(self.ifname)
        self.assertTrue(ifindex > 0)
        name = socket.if_indextoname(ifindex)
        self.assertEqual(self.ifname, name)

        self.assertRaises(TypeError, socket.if_indextoname, None)
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
