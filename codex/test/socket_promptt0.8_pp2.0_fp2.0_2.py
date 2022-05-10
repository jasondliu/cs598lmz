import socket
# Test socket.if_indextoname, socket.if_nametoindex and socket.getifaddrs

import unittest
import errno
import os
import sys
import subprocess
import ctypes

import test.support
from test.support import import_module, get_attribute
IPV6 = import_module('ipaddress')

def get_errno(exc):
    """
    Get the error code from socket.error.
    """
    if isinstance(exc.args, tuple):
        return exc.args[0]
    else:
        return exc.args[1][0]

class NetworkAPITest(unittest.TestCase):

    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockfd = self.sock.fileno()

    def tearDown(self):
        self.sock.close()

