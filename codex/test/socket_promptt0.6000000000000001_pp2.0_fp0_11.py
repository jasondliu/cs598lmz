import socket
# Test socket.if_indextoname() function.
import test.support
import unittest
if_indextoname = socket.if_indextoname
if_nametoindex = socket.if_nametoindex
AF_INET6 = getattr(socket, 'AF_INET6', None)
if AF_INET6 is not None:
    has_ipv6 = True
else:
    has_ipv6 = False

class InterfaceTest(unittest.TestCase):

    @unittest.skipUnless(hasattr(socket, 'if_indextoname'),
        'need socket.if_indextoname()')
    def test_if_indextoname(self):
        self.assertEqual(if_indextoname(1), 'lo')
        self.assertRaises(ValueError, if_indextoname, 0)

    @unittest.skipUnless(hasattr(socket, 'if_nametoindex'),
        'need socket.if_nametoindex()')
    def test_if_nametoindex(self):
        self.assertEqual
