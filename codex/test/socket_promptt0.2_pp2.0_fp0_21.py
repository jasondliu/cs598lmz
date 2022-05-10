import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test.support import run_unittest, TESTFN, unlink

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # On Windows, this test fails if the network is not initialized
        # (i.e. no network cable plugged in).
        ifname = socket.if_indextoname(1)
        self.assertTrue(ifname, 'could not find interface #1')
        self.assertEqual(socket.if_indextoname(1), ifname)
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 2**32)
        self.assertRaises(ValueError, socket.if_indextoname, 2**64)

