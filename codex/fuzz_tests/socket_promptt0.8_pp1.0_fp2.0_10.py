import socket
# Test socket.if_indextoname()
#
# This function can be used to convert an interface index to its corresponding
# network interface name.
#
# Author: Alexander Hultnér, alexander@hultner.se
#

import socket
import unittest

class NetworkInterfacesTest(unittest.TestCase):

    def testIfIndexToName(self):
        """Test if_indextoname()"""
        # Try converting to ifindex of lo using the name of lo
        self.assertEqual(socket.if_indextoname(1), 'lo')

if __name__ == "__main__":
    unittest.main()
