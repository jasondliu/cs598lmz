import socket
# Test socket.if_indextoname()

# This is a simple test that checks if we can use the
# socket.if_indextoname() function to get the interface name
# of the loopback interface.

# The test is skipped if the function is not present.

import test.support
import unittest

class TestIf_indextoname(unittest.TestCase):
    def test_if_indextoname(self):
        if not hasattr(socket, 'if_indextoname'):
            self.skipTest('socket.if_indextoname() not present')
        name = socket.if_indextoname(1)
        self.assertEqual(name, 'lo')

if __name__ == '__main__':
    unittest.main()
