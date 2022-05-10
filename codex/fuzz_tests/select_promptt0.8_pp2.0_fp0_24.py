import select
# Test select.select(), select.epoll(), select.kqueue()
# 3.2+ has select.poll(), but it is not tested
import socket
import sys
import threading
import time
import unittest

from test import support
from test.support import has_xxx, threading_helper


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.evt = threading_helper.initialize_test_server()

    def tearDown(self):
        self.evt.set()
        self.server.join()
        self.evt.clear()
        self.assertFalse(self.evt.is_set(), "Event is set")

    def client_thread(self, conn):
        self.evt.wait()
        conn.send(b"x")
        conn.close()

    def run_case(self):
        sock = socket.socket()
        with support.transient_internet('localhost'):
            port = support.bind_port(sock)
        sock.listen(5)
        _,
