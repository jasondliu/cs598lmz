import select
# Test select.select() on a non-blocking socket

import socket
import select
import unittest
import os
import time

class SelectTest(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = support.bind_port(self.serv)
        self.serv.listen(5)

    def tearDown(self):
        self.serv.close()
        self.serv = None

    def test_basic(self):
        # Test a simple series of operations on a non-blocking socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(0)
        s.connect(("localhost", self.port))
        self.assertEqual(select.select([s],[],[],0), ([s], [], []))
        s.close()

