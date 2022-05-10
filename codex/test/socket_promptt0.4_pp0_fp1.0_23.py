import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        if not hasattr(socket, 'if_indextoname'):
            self.skipTest('socket.if_indextoname() required')
        self.assertEqual(socket.if_indextoname(1), 'lo')
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, -1)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == '__main__':
    test_main()
