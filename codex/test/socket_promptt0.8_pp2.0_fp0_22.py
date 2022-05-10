import socket
# Test socket.if_indextoname() on Windows, when the interfaces are present.

import unittest
import os
from test import support

if not hasattr(socket, "if_indextoname"):
    raise unittest.SkipTest("if_indextoname not defined")

if not hasattr(socket, "IF_NAMESIZE"):
    raise unittest.SkipTest("IF_NAMESIZE not defined")

IPV4_LOOPBACK = "127.0.0.1"
IPV4_ADDRESS = "192.168.1.1"

class IfIndextoNameTests(unittest.TestCase):

    def test_if_indextoname(self):
        name = socket.if_indextoname(1)
        self.assertTrue(name)
        self.assertEqual(len(name), socket.IF_NAMESIZE)

    def test_if_indextoname_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, 0)
