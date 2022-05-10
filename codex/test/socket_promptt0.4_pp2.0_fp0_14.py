import socket
# Test socket.if_indextoname()
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest, socket_helper
try:
    import threading
except ImportError:
    threading = None
try:
    import _thread
except ImportError:
    _thread = None

class BaseNetworkTest(unittest.TestCase):

    def setUp(self):
        if hasattr(socket, 'socket'):
            self.sock = socket.socket()
        else:
            self.sock = None
        self.serv = socket.socket()
        self.port = support.bind_port(self.serv)
        self.serv.listen(5)

    def tearDown(self):
        if self.sock:
            self.sock.close()
        self.serv.close()


class NetworkConnectionNoServer(BaseNetworkTest):

    def testNoServer(self):
        self.serv.close()
        self.assertRaises(ConnectionRefusedError, self.sock.connect, ('localhost', self.port))


