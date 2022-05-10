import socket
# Test socket.if_indextoname() function.

import unittest
import socket
import sys
import os

from test import support
from test.support import run_unittest

class IfIndextonameTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_socket_if_indextoname(self):
        # Test socket.if_indextoname()
        ifname = socket.if_indextoname(1)
        self.assertIsNotNone(ifname)
        self.assertNotEqual(ifname, '')

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == '__main__':
    test_main()
