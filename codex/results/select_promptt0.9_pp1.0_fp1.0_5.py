import select
# Test select.select function on sockets

import socketserver
import time
import unittest

# https://stackoverflow.com/questions/32853962/implementation-of-select-based-on-event-loop

# https://stackoverflow.com/questions/11369064/python-socket-server-select-with-multiple-instances

# select can't be used to monitor stdin but stdin can be used in select for
# windows

# python 2.7 has a bug where if the socket event loop is running in a thread
# select may raise a window error on windows

# python3 seems to have fixed this issue

class Test_select_sockets(unittest.TestCase):

    def setUp(self):
        time.sleep(0.05)

    def test_select_not_implemented(self):
        self.assertRaises(NotImplementedError, select.select, [sys.stdin], [], [])

    def test_select_on_server_port(self):
        # test a waiting server
        # the test will fail
