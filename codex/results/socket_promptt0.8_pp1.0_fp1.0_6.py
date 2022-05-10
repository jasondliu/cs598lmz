import socket
# Test socket.if_indextoname() on Linux.
import unittest
from test import support

if hasattr(socket, 'if_indextoname'):
    class InterfaceTestCase(unittest.TestCase):

        @unittest.skipUnless(hasattr(socket, 'if_nametoindex'),
            'if_nametoindex() required')
        def test_if_nametoindex(self):
            index = socket.if_nametoindex('lo')
            self.assertEqual(socket.if_indextoname(index), 'lo')

        @unittest.skipUnless(hasattr(socket, 'if_nameindex'),
            'if_nameindex() required')
        def test_if_nameindex(self):
            interfaces = socket.if_nameindex()
            for if_index, if_name in interfaces:
                self.assertEqual(socket.if_indextoname(if_index), if_name)
                self.assertEqual(if_index, socket.if_nametoindex(if_name))


if __name__ == '__main__':
