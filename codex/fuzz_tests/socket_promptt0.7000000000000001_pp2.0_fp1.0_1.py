import socket
# Test socket.if_indextoname()
#
# This test only works if the if_nameindex() lookup succeeds.
#

import os, sys
sys.path[1:1] = [os.path.join(sys.path[0], '..')]

from common import support
support.use(__name__)

import socket
import unittest

class TestIfnameindex(unittest.TestCase):

    def test_interface_indextoname(self):

        # A list of all the interface names
        #
        interfaces = [x[1] for x in socket.if_nameindex()]

        # For each interface index, check that its name matches the
        # interface name in the index.
        #
        for i in range(0, len(interfaces)):
            self.assertEqual(socket.if_indextoname(i), interfaces[i])

if __name__ == "__main__":
    unittest.main()
