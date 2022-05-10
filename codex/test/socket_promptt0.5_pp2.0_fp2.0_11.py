import socket
# Test socket.if_indextoname()
from test import support
from test.support import os_helper
from test.support.socket_helper import bind_port
import unittest
from unittest.mock import patch
import warnings


class IfIndextonameTests(unittest.TestCase):

    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = bind_port(self.sock)

    def tearDown(self):
        self.sock.close()

    def test_if_indextoname(self):
        ifname = socket.if_indextoname(
            socket.if_nametoindex(support.IFNAME))
        self.assertEqual(ifname, support.IFNAME)

    def test_if_indextoname_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, -1)

