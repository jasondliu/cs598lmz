import select
# Test select.select() with a non-blocking file descriptor.
import os
import time
import unittest
from select import error as SelectError
from select import POLLIN, POLLOUT, POLLHUP, POLLERR, POLLNVAL
from test import support
with support.transient_internet('www.python.org'):
    import socket
POLLIN_ERR = POLLIN | POLLERR | POLLHUP | POLLNVAL


class PollTests(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = support.bind_port(self.serv)
        self.serv.listen(5)
        self.con, addr = self.serv.accept()
        self.p = select.poll()
        self.p.register(self.con, POLLIN_ERR)

    def tearDown(self):
        self.p.unregister(self.con)
        self.con.close()
        self.
