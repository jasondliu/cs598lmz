import socket
# Test socket.if_indextoname()

import unittest
from test import support
from test.support import find_unused_port

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # This test requires the host to have at least two network
        # interfaces.
        if_indextoname = socket.if_indextoname
        if_nametoindex = socket.if_nametoindex
        if_nameindex = socket.if_nameindex
        if len(if_nameindex()) < 2:
            self.skipTest('need at least two network interfaces')
        #
        name = if_indextoname(if_nametoindex(if_nameindex()[0][1]))
        self.assertTrue(name)
        self.assertEqual(if_nametoindex(name),
                         if_nametoindex(if_nameindex()[0][1]))
        self.assertRaises(ValueError, if_indextoname, -1)
