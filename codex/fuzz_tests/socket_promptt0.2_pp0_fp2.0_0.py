import socket
# Test socket.if_indextoname()
#
# This test case is to check if the function socket.if_indextoname()
# works as expected.
#
# The function is supposed to return the name of the interface
# corresponding to the given index.
#
# Author: Sowmini Varadhan <sowmini.varadhan@oracle.com>

import os
import sys
import socket
import struct
import array
import fcntl
import unittest
import errno

import test.test_support

SIOCGIFNAME = 0x8910

class IfIndexToNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        """Test if_indextoname()"""

        # Get the list of interfaces
        ifnames = socket.if_nameindex()

        # Get the list of interface indices
        ifindices = [i[0] for i in ifnames]

        # Get the list of interface names
        ifnames = [i[1] for i in ifnames]

        # Check if the interface names returned by if_ind
