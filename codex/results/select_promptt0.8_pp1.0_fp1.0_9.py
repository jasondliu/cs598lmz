import select
# Test select.select() with a file descriptor that has a buffer.
import os
import select
import socket
import unittest
from test.support import find_unused_port, run_unittest, bind_port
TESTENTRY = 'www.python.org'.encode()
TESTPORT = 80
TESTDATA = b'GET /index.html HTTP/1.0\n\n'
HOST = b'localhost'
TESTENTRY = HOST
BUFSIZE = 1024

class BufferTest(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = bind_port(self.serv)
        self.serv.listen(5)
        self.cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cli.connect((HOST, self.port))
        self.set_server()
        self.set_client()

    def tearDown(self):
        self.cli.close()
