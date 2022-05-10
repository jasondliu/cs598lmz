import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertEqual(socket.if_indextoname(1), 'lo')
        self.assertEqual(socket.if_indextoname(2), 'eth0')
        self.assertEqual(socket.if_indextoname(3), 'eth1')
        self.assertEqual(socket.if_indextoname(4), 'sit0')
        self.assertEqual(socket.if_indextoname(5), 'wlan0')
        self.assertEqual(socket.if_indextoname(6), 'wlan1')
        self.assertEqual(socket.if_indextoname(7), 'vmnet1')
        self.assertEqual(socket.if_indextoname(8), 'vmnet8')
