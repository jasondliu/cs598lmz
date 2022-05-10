import socket
# Test socket.if_indextoname()

from test_support import get_attribute, verbose
import unittest, os

class IfconfTestCase(unittest.TestCase):

    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def tearDown(self):
        self.sock.close()

    def test_if_name(self):
        self.assertTrue(isinstance(self.sock.if_name, basestring),
                "if_name is not a string")

    def test_if_index(self):
        self.assertTrue(isinstance(self.sock.if_index, int),
                "if_index is not an integer")

