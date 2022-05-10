import socket
# Test socket.if_indextoname() and socket.if_nameindex()
#
# This test is not exhaustive and relies on the host having a
# network interface.
#
# TODO: test for other errors and more interfaces.
#

import unittest
import socket
import errno

class If_Indextoname_Test(unittest.TestCase):

    def test_ifindextoname(self):
        name = socket.if_indextoname(1)
        self.assertTrue(name is not None)

    def test_ifindextoname_error(self):
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)

    def test_ifnameindex(self):
        names = socket.if_nameindex()
        self.assertTrue(isinstance(names, list))
        self.assertTrue(len(names) > 0)
        self.assertTrue(isinstance(names[0], tuple))
        self.assertE
