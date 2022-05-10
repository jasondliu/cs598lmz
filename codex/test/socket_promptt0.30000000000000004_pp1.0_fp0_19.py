import socket
# Test socket.if_indextoname()

import sys
import os
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        if_indextoname = socket.if_indextoname
        if_nametoindex = socket.if_nametoindex
        try:
            ifname = if_indextoname(1)
        except OSError:
            # This can fail on Windows, e.g. if no network interface is
            # installed.
            return
        self.assertEqual(if_nametoindex(ifname), 1)
        self.assertRaises(OSError, if_indextoname, 0)
        self.assertRaises(OSError, if_indextoname, -1)
        self.assertRaises(OSError, if_indextoname, 2**32)
        self.assertRaises(OSError, if_indextoname, '1')
