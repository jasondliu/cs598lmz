import socket
# Test socket.if_indextoname()

import unittest
import socket

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertEqual(socket.if_indextoname(1), 'lo')

if __name__ == '__main__':
    unittest.main()
