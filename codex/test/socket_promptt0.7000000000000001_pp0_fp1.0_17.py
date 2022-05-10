import socket
# Test socket.if_indextoname
#
# On Linux, if_indextoname is just an alias for if_indextoname so 
# only test if_indextoname
#
import os
if os.uname()[0] == 'Linux':
    raise ImportError("Use the if_indextoname test instead")

import unittest
from test.support import run_unittest, find_unused_port

class IfIndextonameTest(unittest.TestCase):

    def test_basic(self):
        # Verify that the socket is really using the loopback interface
        port = find_unused_port()
        s = socket.socket()
        s.bind(("127.0.0.1", port))
        # Find the index for the loopback interface
        index = socket.if_nametoindex("lo0")
        # Find the name for the loopback interface
        name = socket.if_indextoname(index)
        self.assertEqual(name, "lo0")

