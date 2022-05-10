import select
# Test select.select() on a socket.

import socket
import unittest
from test.support import socket_helper
from test.support import run_unittest
from test import support

# On some systems, select.select() is broken when used on a socket.
# This is true on HP-UX 11.00 with Python 1.5.2.  It may also be
# true on Linux 2.0.x kernels.  It is fixed on Linux 2.1.x kernels.
# This test ensures that the bug is fixed.

# This test must be run with a timeout of at least 2 seconds.

HOST = support.HOST

class SelectTest(unittest.TestCase):
    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = socket_helper.bind_port(self.serv)
        self.serv.listen(5)

    def tearDown(self):
        self.serv.close()
        self.serv = None

    def client(self):
        return
