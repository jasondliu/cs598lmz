import socket
# Test socket.if_indextoname()

import os
if os.name == 'nt' or sys.platform == 'cygwin':
    print("Can't test socket.if_indextoname() on", os.name)
    sys.exit(0)

import unittest
from test import support

import socket

class IfIndextonameTest(unittest.TestCase):

    def test_success(self):
        # Issue #8050:
        # On some systems (e.g. Mac OS X) some interfaces don't have IPv4
        # addresses.  In that case, the socket module is supposed to skip
        # the interface in question.
        interfaces = [x for x in socket.if_indextoname(i, 0)
                      for i in range(256) if x]
        self.assertTrue(interfaces)

    def test_invalid_index(self):
        self.assertRaises(ValueError, socket.if_indextoname, -1, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 256, 0)
