import socket
# Test socket.if_indextoname()
#
# This test should be skipped if the function is not available.
import unittest
from test import support

class If_indextonameTest(unittest.TestCase):

    def test_badfmt(self):
        for badfmt in [ '', '#', '123', '1234567890123456789012345',
                        '1\x00' ]:
            self.assertRaises(ValueError, socket.if_indextoname, badfmt)

    def test_badfmt_bytes(self):
        for badfmt in [ b'', b'#', b'123', b'1234567890123456789012345',
                        b'1\x00' ]:
            self.assertRaises(ValueError, socket.if_indextoname, badfmt)

    def test_basic(self):
        for ifname in socket.if_nameindex():
            self.assertEqual(socket.if_indextoname(ifname[0]), ifname[1])

    @support
