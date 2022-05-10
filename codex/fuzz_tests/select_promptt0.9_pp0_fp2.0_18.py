import select
# Test select.select() behavior on closed socket fd

import socket
import os
import unittest

SOCKNAME = "select.sock"

class SelectTest(unittest.TestCase):
    def setUp(self):
        os.unlink(SOCKNAME)
        self.serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.serv.bind(SOCKNAME)
        self.serv.listen(1)

    def tearDown(self):
     
