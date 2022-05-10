import select
# Test select.select() and select.poll()

import os
import select
import socket
import time
import unittest

class SelectTestCase(unittest.TestCase):
    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = test_support.bind_port(self.serv)
        self.serv.listen(1)

        self.con, self.cli = socket.socketpair()
        self.serv.setblocking(0)
        self.con.setblocking(0)
        self.cli.setblocking(0)

    def tearDown(self):
        self.serv.close()
        self.con.close()
        self.cli.close()

    def test_error_conditions(self):
        # Testing exceptional conditions
        self.assertRaises(TypeError, select.select, 1, 2, 3)
        self.assertRaises(TypeError, select.select, [1], 2, 3)
