import socket
# Test socket.if_indextoname()
import struct
import sys
import unittest

import test.test_support

class IfIndexTests(unittest.TestCase):

    def test_if_indextoname(self):
        """Test if_indextoname()."""
        self.assertEqual(socket.if_indextoname(1), 'lo')

    @unittest.skipUnless(hasattr(socket, 'if_nameindex'),
                         'if_nameindex not available')
    def test_if_nameindex(self):
        """Test if_nameindex()."""
        idxlist = socket.if_nameindex()
        lo_idx = -1
        for idx, ifname in idxlist:
            if ifname == 'lo':
                lo_idx = idx
                break
        else:
            self.fail('lo interface not found')
        self.assertEqual(socket.if_indextoname(lo_idx), 'lo')

    def test_if_nametoindex(self):
        """Test if_nameto
