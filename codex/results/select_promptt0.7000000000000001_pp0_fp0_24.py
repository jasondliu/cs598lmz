import select
# Test select.select for edge-triggered behavior.
#
# On Linux, select (and poll) are level-triggered: they will return a poll
# object each time the state of one of its file descriptors changes.
#
# On Windows, select (and poll) are edge-triggered: they will return a poll
# object at most once for each state change.

import socket
import unittest
from test import support

class SelectEdgeTriggerTest(unittest.TestCase):
    def setUp(self):
        self.server = socket.socket()
        self.server.setblocking(False)
        self.server.bind(('', 0))
        self.server.listen(5)
        self.port = self.server.getsockname()[1]

        self.client = socket.socket()
        self.client.setblocking(False)
        self.client.connect_ex(('localhost', self.port))

    def tearDown(self):
        self.client.close()
        self.server.close()

    def test_select(self):
        r
