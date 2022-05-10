import select
# Test select.select with a list of sockets.
from test import test_support
import time
import unittest
from test.test_support import TESTFN, run_unittest, reap_children

HOST = test_support.HOST

class SelectTestCase(unittest.TestCase):
    def setUp(self):
        self.serv_conn = None
        self.cli_conn = None
        self.port = test_support.bind_port(HOST)

    def tearDown(self):
        if self.serv_conn is not None:
            self.serv_conn.close()
            self.serv_conn = None
        if self.cli_conn is not None:
            self.cli_conn.close()
            self.cli_conn = None
        test_support.reap_children()

    def test_select(self):
        # Set up two sockets
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.setblocking(0)
        serv.bind((HOST, self.port))
        serv.
