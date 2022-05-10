import socket
# Test socket.if_indextoname()

import unittest
import socket
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertEqual(socket.if_indextoname(1), 'lo')
        self.assertEqual(socket.if_indextoname(2), 'eth0')
        self.assertEqual(socket.if_indextoname(3), 'sit0')
        self.assertEqual(socket.if_indextoname(4), 'ip6tnl0')

    def test_if_indextoname_invalid(self):
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 5)

if __name__ == '__main__':
    unittest.main()
