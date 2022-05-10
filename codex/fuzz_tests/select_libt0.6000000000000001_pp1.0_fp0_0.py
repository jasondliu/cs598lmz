import select
import socket
import sys
import threading
import time
import unittest
from unittest import mock

from tests import utils


class TCPServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_address = 'localhost', 0
        cls.server = utils.TCPServer(cls.server_address, utils.EchoRequestHandler)
        cls.server_thread = threading.Thread(
            target=cls.server.serve_forever,
            # Short poll interval to make the test finish quickly.
            # Time between requests is short enough that we won't wake
            # up spuriously too many times.
            kwargs={'poll_interval':0.01},
            daemon=True,
        )
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()

   
