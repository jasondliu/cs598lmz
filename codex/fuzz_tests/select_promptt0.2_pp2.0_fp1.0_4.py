import select
# Test select.select()
#
# This test is not very good, but it is better than nothing.
#
# It tests that select.select() returns the expected results.
# It does not test that select.select() actually waits for the
# specified amount of time.

import select
import socket
import time
import unittest

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = test_support.bind_port(self.serv)
        self.serv.listen(5)

    def tearDown(self):
        self.serv.close()
        self.serv = None

    def test_returned_list_identity(self):
        # Check that the lists returned by select() are the same objects
        # as the lists given as arguments.
        r, w, x = [self.serv], [], []
        r2, w2, x2 = select.select(r, w, x)
        self.assertTrue(
