import socket
# Test socket.if_indextoname()
#
# This test case is for verifying the behavior of socket.if_indextoname()
# when the index passed in is not a valid index.
#
# Author: Sowmini Varadhan
# Date: October, 2017

import os
import sys
import unittest
import errno
import platform
import socket

from test.support import run_unittest, HAS_IPV6

@unittest.skipUnless(HAS_IPV6, 'IPv6 required for this test.')
class If_indextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        """Test socket.if_indextoname()"""
        if_index = -1
        if_name = socket.if_indextoname(if_index)
        self.assertEqual(if_name, None)

if __name__ == "__main__":
    unittest.main()
