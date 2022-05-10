import socket
# Test socket.if_indextoname() (GH#30)
try:
    socket.if_indextoname(1)
except ValueError:
    pass
except AttributeError:
    raise unittest.SkipTest("platform lacks if_indextoname")

import pandas as pd
import numpy as np
import time

from test.util import assert_frame_equal


class TestTcpServer(unittest.TestCase):
    def setUp(self):
        self.server = pyarrow.TcpServer()

    def test_start_and_stop(self):
        self.server = pyarrow.TcpServer()
        self.server.start()
        self.server.stop()


class TestTcpStream(unittest.TestCase):
    def setUp(self):
        self.server = pyarrow.TcpServer()
        self.hostname = socket.getfqdn()

    def tearDown(self):
        self.server.stop()

    def test_connect(self):
        self.server.start()

        reader = pyarrow.TcpReader
