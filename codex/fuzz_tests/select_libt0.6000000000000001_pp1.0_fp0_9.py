import select
import socket
import struct
import sys
import time
import unittest
import errno

from test import support
from test.support import TESTFN, run_unittest, requires_mac_ver, import_module

@unittest.skipUnless(hasattr(socket, "socketpair"),
                     "socket module has no socketpair() method")
class SocketPairTestCase(unittest.TestCase):

    def test_basic(self):
        sv = socket.socketpair()
        self.addCleanup(sv[0].close)
        self.addCleanup(sv[1].close)
        self.assertEqual(type(sv), type([]))
        self.assertEqual(len(sv), 2)
        self.assertIsInstance(sv[0], socket.socket)
        self.assertIsInstance(sv[1], socket.socket)

    def test_type(self):
        # Issue #11343: socketpair() must return sockets of the same type
        sv = socket.socketpair()
        self.addCleanup(sv[0].close)
