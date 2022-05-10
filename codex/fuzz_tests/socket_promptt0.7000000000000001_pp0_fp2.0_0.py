import socket
# Test socket.if_indextoname()

import unittest, socket

class IfIndextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        names = socket.if_indextoname(1)
        self.assertTrue(names)
        self.assertIn(names, socket.if_nameindex())
        self.assertRaises(OverflowError, socket.if_indextoname, -1)

if __name__ == '__main__':
    unittest.main()
