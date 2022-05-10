import select
# Test select.select.
# select.select is a general purpose select mechanism.  It returns
# lists of objects that are ready for some type of I/O.  It can be
# used to do synchronous I/O.  It can be used to wait for a socket to
# become readable or writable.  It can also be used to wait for a
# file descriptor to become readable or writable.  It is also used by
# FileSelector.

import socket
import time
import select

import unittest
from test import support

HAVE_SOCKET_TIMEOUT = hasattr(socket, 'settimeout')

class SelectTestCaseBase:
    def setUp(self):
        self.serv = socket.socket()
        self.port = support.bind_port(self.serv)
        self.serv.listen(5)
        self.con, addr = self.serv.accept()
        self.r, self.w = os.pipe()
        self.r2, self.w2 = os.pipe()

    def tearDown(self):
        self.r2, self.
