import socket
# Test socket.if_indextoname and socket.if_nameindex
import threading
import time
import unittest
from test import support

import _socket

support.import_module('select')

class GeneralModuleTests(unittest.TestCase):

    def test_socket_module(self):
        s = socket.socket()
        self.assertEqual(type(s), socket.socket)

    def test_repr(self):
        self.assertTrue(repr(socket.socket).startswith("<class '_socket.socket'>"))
        s = socket.socket()
        self.assertTrue(repr(s).startswith("<socket.socket fd="))

    def test_helper(self):
        self.assertTrue(repr(socket.AF_INET).startswith("<AddressFamily.AF_INET:"))

    def test_attributes(self):
        self.assertEqual(socket.has_ipv6, hasattr(_socket, "has_ipv6"))
        s = socket.socket()
        self.assertTrue(hasattr
