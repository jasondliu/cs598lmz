import socket
# Test socket.if_indextoname()
#
# This is a reverse lookup from the interface index to the interface name
#
# This test assumes the interface index for "lo" is 1
#
# This test will fail on Windows as it doesn't have a "lo" interface.

import unittest
import socket

class NetworkInterfaceNamesTest(unittest.TestCase):

    def test_if_indextoname(self):
        if_name = socket.if_indextoname(1)
        self.assertTrue(if_name == 'lo', "if_indextoname(1) should return 'lo'")

if __name__ == '__main__':
    unittest.main()
