import select
import socket
import sys
import time
import traceback
import unittest

from test import support
from test.support import import_module, verbose

# Skip these tests if there is no socket module.
socket = import_module('socket')

HOST = support.HOST
MSG = b'Michael Gilfix was here\n'
BUFSIZE = 1024

#
# Test the socket module
#
class SocketTCPTest(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = support.bind_port(self.serv)
        self.serv.listen(5)

    def tearDown(self):
        self.serv.close()
        self.serv = None

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, self.port))
        return sock

    def testTimeoutDefault(self):
        # Testing
