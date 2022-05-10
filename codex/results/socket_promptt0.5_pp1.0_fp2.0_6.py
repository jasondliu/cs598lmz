import socket
# Test socket.if_indextoname()

import unittest
from test import support
from socket import AF_INET, AF_INET6, if_indextoname, if_nameindex
from socket import if_nametoindex

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertRaises(ValueError, if_indextoname, -1, AF_INET)
        self.assertRaises(ValueError, if_indextoname, -1, AF_INET6)
        self.assertRaises(ValueError, if_indextoname, -1, AF_INET6, 1)
        self.assertRaises(ValueError, if_indextoname, -1, AF_INET, 1)

        # Test for the case when there is no interface of the given family
        # installed.
        if_nameindex()
        for family in (AF_INET, AF_INET6):
            self.assertEqual(None, if_indextoname(1, family))

