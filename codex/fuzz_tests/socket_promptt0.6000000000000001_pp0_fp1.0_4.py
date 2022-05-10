import socket
# Test socket.if_indextoname()
#
# See also http://bugs.python.org/issue7679

import socket
import unittest

from test import support

class IfIndexTest(unittest.TestCase):

    def setUp(self):
        self.sock = socket.socket()

    def tearDown(self):
        self.sock.close()

    def test_if_indextoname(self):
        # XXX: some valid interface on your machine
        ifname = socket.if_indextoname(1)
        self.assertIsInstance(ifname, str)

    def test_if_nametoindex(self):
        # XXX: some valid interface on your machine
        index = socket.if_nametoindex('lo')
        self.assertIsInstance(index, int)

    def test_if_nameindex(self):
        # XXX: some valid interface on your machine
        nameindex = socket.if_nameindex()
        self.assertIsInstance(nameindex, list)
        self.assertIsInstance(nameindex[0], tuple)
        self.assert
